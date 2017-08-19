import os
from flask import Blueprint, jsonify
from common import get_entered_text, requires_auth
from environment import LOCAL_ENVS, SIT_URL, E2E_URL, CLAIM_BASE_URL
from warning import ENV_WARNING

claim_app = Blueprint('claim_app', __name__)

@claim_app.route('/claim', methods=['POST'])
@requires_auth
def get_claims_env():
    env = get_entered_text()
    return jsonify(
        text=get_claims_url(env),
        response_type="in_channel"
    )

def get_claims_url(env):
    if env in LOCAL_ENVS:
        return CLAIM_BASE_URL % env
    elif env == 'sit':
        return SIT_URL % 'claims'
    elif env == 'e2e':
        return E2E_URL % 'claims'
    else:
        return ENV_WARNING
