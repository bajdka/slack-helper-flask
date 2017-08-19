import os
from flask import Blueprint, jsonify
from common import get_entered_text, requires_auth
from environment import LOCAL_ENVIRONMENTS, SIT_ENV_URL, E2E_ENV_URL, ENV_WARNING, CLAIM_BASE_URL

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
    if env in LOCAL_ENVIRONMENTS:
        return CLAIM_BASE_URL % env
    elif env == 'sit':
        return SIT_ENV_URL % 'claims'
    elif env == 'e2e':
        return E2E_ENV_URL % 'claims'
    else:
        return ENV_WARNING
