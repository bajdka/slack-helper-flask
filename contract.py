from flask import Blueprint
from common import requires_auth
from environment import ALL_ENVS, CONTRACT_MODULE, get_url
from warning import ENV_WARNING
from message import send_slack_message, get_entered_text

contract_app = Blueprint('contract_app', __name__)


@contract_app.route('/contract', methods=['POST'])
@requires_auth
def get_contract_env():
    env = get_entered_text()
    if env in ALL_ENVS:
        return send_slack_message(get_url(CONTRACT_MODULE, env))
    else:
        return ENV_WARNING
