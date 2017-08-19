from flask import Blueprint
from common import requires_auth
from environment import ALL_ENVS, WPC_MODULE, get_url
from warning import ENV_WARNING
from message import send_slack_message, get_entered_text

wpc_app = Blueprint('wpc_app', __name__)

@wpc_app.route('/wpc', methods=['POST'])
@requires_auth
def get_wpc_env():
    env = get_entered_text()
    if env in ALL_ENVS:
        return send_slack_message(get_url(WPC_MODULE, env))
    else:
        return ENV_WARNING
