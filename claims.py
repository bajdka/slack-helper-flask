import os
from flask import Blueprint, jsonify
from common import get_entered_text, requires_auth
from environment import ALL_ENVS, CLAIM_MODULE, get_url
from warning import ENV_WARNING

claim_app = Blueprint('claim_app', __name__)

@claim_app.route('/claim', methods=['POST'])
@requires_auth
def get_claims_env():
    env = get_entered_text()
    if env in ALL_ENVS:
        return jsonify(
            text=get_url(CLAIM_MODULE, env),
            response_type="in_channel"
        )
    else:
        return ENV_WARNING
