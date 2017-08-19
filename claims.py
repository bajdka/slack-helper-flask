import os
from flask import Blueprint
from common import requires_auth
from environment import ALL_ENVS, CLAIM_MODULE, get_url
from warning import ENV_WARNING
from message import send_slack_message, get_entered_text

claim_app = Blueprint('claim_app', __name__)

@claim_app.route('/claim', methods=['POST'])
@requires_auth
def get_claims_env():
    env = get_entered_text()
    if env in ALL_ENVS:
        return send_slack_message(get_url(CLAIM_MODULE, env))
    else:
        return ENV_WARNING
