import os
import re
from flask import Blueprint
from common import requires_auth
from warning import JIRA_WARNING
from message import get_entered_text, send_slack_message

JIRA_BASE_URL = os.environ['JIRA_BASE_URL']

jira_app = Blueprint('jira_app', __name__)


@jira_app.route('/jira', methods=['POST'])
@requires_auth
def get_jira_link():
    jira_task_number = get_entered_text()
    if is_number_correct(jira_task_number):
        return send_slack_message(get_jira_url(jira_task_number))
    else:
        return JIRA_WARNING


def get_jira_url(task_number):
    return JIRA_BASE_URL % task_number


def is_number_correct(jira_task_number):
    return re.match("^[0-9]{4}$", jira_task_number)
