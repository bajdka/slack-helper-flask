from flask import Blueprint, jsonify
from common import get_entered_text, requires_auth
from environment import LOCAL_ENVIRONMENTS, ENV_WARNING, CONTRACT_BASE_URL

contract_app = Blueprint('contract_app', __name__)

@contract_app.route('/contract', methods=['POST'])
@requires_auth
def get_contract_env():
    env = get_entered_text()
    if env in LOCAL_ENVIRONMENTS:
        return jsonify(
            text=get_local_contract_url(env),
            response_type="in_channel"
            )
    else:
        return ENV_WARNING

def get_local_contract_url(env):
    return CONTRACT_BASE_URL % env
