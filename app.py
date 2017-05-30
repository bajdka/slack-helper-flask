from flask import Flask, request, Response
from functools import wraps
import os

SLACK_WEBHOOK_SECRET = os.environ['SLACK_WEBHOOK_SECRET']
BASE_URL = 'http://cgbsclaim%s01:18001/claims/overview'

app = Flask(__name__)

def get_claims_url(env): 
    return BASE_URL % env

def check_auth():
    return request.form.get('token') == SLACK_WEBHOOK_SECRET

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not check_auth():
            return Response(), 401
        return f(*args, **kwargs)
    return decorated

@app.route('/')
def homepage():
    return "sup?"

@app.route('/dev', methods=['POST'])
@requires_auth
def get_dev_env():
    return get_claims_url('dev')

@app.route('/qa', methods=['POST'])
@requires_auth
def get_qa_env():
    return get_claims_url('qa')

@app.route('/test', methods=['POST'])
def get_test_env():
    return get_claims_url('test')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
