from flask import Blueprint
from common import requires_auth
from message import send_slack_message
from tools import E2E_ALL_URLS

e2e_app = Blueprint('e2e_app', __name__)


@e2e_app.route('/e2e', methods=['POST'])
@requires_auth
def get_e2e_all_url():
    return send_slack_message(E2E_ALL_URLS)
