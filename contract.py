from flask import Blueprint, jsonify
from common import get_entered_text, requires_auth
from environment import ALL_ENVS, CONTRACT_MODULE, get_url
from warning import ENV_WARNING

contract_app = Blueprint('contract_app', __name__)

@contract_app.route('/contract', methods=['POST'])
@requires_auth
def get_contract_env():
    env = get_entered_text()
    if env in ALL_ENVS:
        return jsonify(
            text=get_url(CONTRACT_MODULE, env),
            response_type="in_channel"
        )
    else:
        return ENV_WARNING
