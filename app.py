from flask import Flask
from datetime import datetime

SLACK_WEBHOOK_SECRET = os.environ('SLACK_WEBHOOK_SECRET')

base_url = 'http://cgbsclaim%s01:18001/claims/overview'

app = Flask(__name__)

def get_claims_url(env): 
    return base_url % env

def is_authenticated(request): 
        return request.form.get('token') == SLACK_WEBHOOK_SECRET

@app.route('/')
def homepage():
    return "sup?"

@app.route('/dev', methods=['POST'])
def get_dev_env():
    if is_authenticated(request):
        return get_claims_url('dev')

@app.route('/qa', methods=['POST'])
def get_qa_env():
    if is_authenticated(request):
        return get_claims_url('qa')

@app.route('/test', methods=['POST'])
def get_test_env():
    return get_claims_url('test')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)