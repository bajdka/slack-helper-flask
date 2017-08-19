from flask import Blueprint
from common import requires_auth
from message import send_slack_message
from tools import SIT_ALL_URLS

sit_app = Blueprint('sit_app', __name__)


@sit_app.route('/sit', methods=['POST'])
@requires_auth
def get_sit_all_url():
    return send_slack_message(SIT_ALL_URLS)
