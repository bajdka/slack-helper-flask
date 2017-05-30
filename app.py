from functools import wraps
import os
import re
from flask import Flask, request, Response

SLACK_WEBHOOK_SECRET = os.environ['SLACK_WEBHOOK_SECRET']
CLAIMS_BASE_URL = 'http://cgbsclaim%s01:18001/claims/overview'
CONTRACT_BASE_URL = 'http://cgbscontract%s01.cg.internal:18001/contracts/overview'
JIRA_URL = 'https://jira.cargarantie.com/browse/BESTIMPL-%s'
ENV_WARNING = 'You crazy? Provide correct environment (dev/qa/uat/test)'
JIRA_WARNING = 'You crazy? Provide correct JIRA task number (e.g. 3242)'
ENVIRONMENTS = ['dev', 'qa', 'test', 'uat']

app = Flask(__name__)

def get_claims_url(env):
    return CLAIMS_BASE_URL % env

def get_contract_url(env):
    return CONTRACT_BASE_URL % env

def get_jira_url(task_number):
    return JIRA_URL % task_number

def get_entered_text():
    return request.form.get('text').lower()

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
        return get_claims_url(env)
    else:
        return ENV_WARNING

@app.route('/contract', methods=['POST'])
@requires_auth
def get_contract_env():
    env = get_entered_text()
    if env in ENVIRONMENTS:
        return get_contract_url(env)
    else:
        return ENV_WARNING

@app.route('/jira', methods=['POST'])
@requires_auth
def get_jira_link():
    jira_task_number = get_entered_text()
    if re.match("^[0-9]{4}$", jira_task_number):
        return get_jira_url(jira_task_number)
    else:
        return JIRA_WARNING

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
