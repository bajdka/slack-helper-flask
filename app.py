from functools import wraps
import os
from flask import Flask, request, Response
import re

SLACK_WEBHOOK_SECRET = os.environ['SLACK_WEBHOOK_SECRET']
BASE_URL = 'http://cgbsclaim%s01:18001/claims/overview'
JIRA_URL = 'https://jira.cargarantie.com/browse/BESTIMPL-%s'

app = Flask(__name__)

def get_claims_url(env):
    return BASE_URL % env

def get_jira_url(task_number):
    return JIRA_URL % task_number

def is_authorized():
    return request.form.get('token') == SLACK_WEBHOOK_SECRET

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not is_authorized():
            return Response(), 401
        return f(*args, **kwargs)
    return decorated

@app.route('/dev', methods=['POST'])
@requires_auth
def get_dev_env():
    return get_claims_url('dev')

@app.route('/qa', methods=['POST'])
@requires_auth
def get_qa_env():
    return get_claims_url('qa')

@app.route('/test', methods=['POST'])
@requires_auth
def get_test_env():
    return get_claims_url('test')

@app.route('/jira', methods=['POST'])
@requires_auth
def get_jira_link():
    jira_task_number = request.form.get('text')
    pattern = re.compile("\b[0-9]\{4\}\b")
    if pattern.match(jira_task_number):
        return get_jira_url(jira_task_number)
    else:
        return 'You crazy? Provide JIRA task number, eg.: 3242'

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
