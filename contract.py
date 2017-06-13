import os
from flask import Blueprint, jsonify
from common import get_entered_text, ENVIRONMENTS, ENV_WARNING, requires_auth

contract_app = Blueprint('contract_app', __name__)

CONTRACT_BASE_URL = os.environ['CONTRACT_BASE_URL']

def get_contract_url(env):
    return CONTRACT_BASE_URL % env

@contract_app.route('/contract', methods=['POST'])
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

