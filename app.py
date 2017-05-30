from flask import Flask
from datetime import datetime

base_url = 'http://cgbsclaim%s01:18001/claims/overview'

app = Flask(__name__)

def get_claims_url(env): 
    return base_url % env

@app.route('/')
def get_url():
    return "sup?"

@app.route('/dev')
def get_dev_env():
    return get_claims_url('dev')

@app.route('/qa')
def get_qa_env():
    return get_claims_url('qa')

@app.route('/test')
def get_test_env():
    return get_claims_url('test')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)