from functools import wraps
import os
import re
from flask import Flask, request, Response, jsonify

SLACK_WEBHOOK_SECRET = os.environ['SLACK_WEBHOOK_SECRET']
CLAIM_BASE_URL = os.environ['CLAIM_BASE_URL']
CONTRACT_BASE_URL = os.environ['CONTRACT_BASE_URL']
JIRA_BASE_URL = os.environ['JIRA_BASE_URL']
ENV_WARNING = 'You crazy? Provide correct environment (dev/qa/uat/test)'
JIRA_WARNING = 'You crazy? Provide correct JIRA task number (e.g. 3242)'
ENVIRONMENTS = ['dev', 'qa', 'test', 'uat']

app = Flask(__name__)

def get_claims_url(env):
    return CLAIM_BASE_URL % env

def get_contract_url(env):
    return CONTRACT_BASE_URL % env

def get_jira_url(task_number):
    return JIRA_BASE_URL % task_number

def get_entered_text():
    return request.form.get('text').lower()

def get_username():
    return request.form.get('username')

def is_authorized():
    return request.form.get('token') == SLACK_WEBHOOK_SECRET
    # return True

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not is_authorized():
            return Response(), 401
        return f(*args, **kwargs)
    return decorated

@app.route('/claim', methods=['POST'])
@requires_auth
def get_claims_env():
    env = get_entered_text()
    if env in ENVIRONMENTS:
        return jsonify(
            text=get_claims_url(env),
            response_type="in_channel"
        )
    else:
        return ENV_WARNING

@app.route('/contract', methods=['POST'])
@requires_auth
def get_contract_env():
    env = get_entered_text()
    if env in ENVIRONMENTS:
        return jsonify(
            text=get_contract_url(env),
            response_type="in_channel"
            )
    else:
        return ENV_WARNING

@app.route('/jira', methods=['POST'])
@requires_auth
def get_jira_link():
    jira_task_number = get_entered_text()
    if re.match("^[0-9]{4}$", jira_task_number):
        return jsonify(
            text=get_jira_url(jira_task_number),
            response_type="in_channel"
            )
    else:
        return JIRA_WARNING

@app.route('/kudo', methods=['POST'])
@requires_auth
def send_kudo():
    response_url = request.form.get('response_url')
    request.post(response_url, headers={'Content-Type': 'application/json'}, data=jsonify(
        text="%s + %s" % (get_entered_text(), request.form.get('user_name')),
        response_type="in_channel"
        ))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
