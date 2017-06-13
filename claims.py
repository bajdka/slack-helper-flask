import os
from flask import Blueprint, jsonify
from common import get_entered_text, ENVIRONMENTS, ENV_WARNING, requires_auth


CLAIM_BASE_URL = os.environ['CLAIM_BASE_URL']

claim_app = Blueprint('claim_app', __name__)

def get_claims_url(env):
    return CLAIM_BASE_URL % env

@claim_app.route('/claim', methods=['POST'])
@requires_auth
def get_claims_env():
    env = get_entered_text()
    if env in ENVIRONMENTS:
        return jsonify(
            text=get_claims_url(env),
            response_type="in_channel"
        )
    else:
        return ENV_WARNING
