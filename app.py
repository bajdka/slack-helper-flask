from flask import Flask, request, Response
from flask_httpauth import HTTPBasicAuth
import os

SLACK_WEBHOOK_SECRET = os.environ['SLACK_WEBHOOK_SECRET']
BASE_URL = 'http://cgbsclaim%s01:18001/claims/overview'

app = Flask(__name__)
auth = HTTPBasicAuth()

def get_claims_url(env): 
    return BASE_URL % env

@auth.slack_token_required
def is_authenticated():
    return request.form.get('token') == SLACK_WEBHOOK_SECRET

@app.route('/')
def homepage():
    return "sup?"

@app.route('/dev', methods=['POST'])
@auth.slack_token_required
def get_dev_env():
    return get_claims_url('dev')

@app.route('/qa', methods=['POST'])
@auth.slack_token_required
def get_qa_env():
    return get_claims_url('qa')

@app.route('/test', methods=['POST'])
def get_test_env():
    return get_claims_url('test')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
