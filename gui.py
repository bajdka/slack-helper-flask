from flask import Blueprint
from common import requires_auth
from message import send_slack_message
from tools import MOCKUPS_WIKI_URL

gui_app = Blueprint('gui_app', __name__)


@gui_app.route('/gui', methods=['POST'])
@requires_auth
def get_mockups_url():
    return send_slack_message(MOCKUPS_WIKI_URL)
