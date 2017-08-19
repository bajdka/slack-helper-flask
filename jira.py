import os
import re
from flask import Blueprint, jsonify
from common import get_entered_text, requires_auth

JIRA_BASE_URL = os.environ['JIRA_BASE_URL']
JIRA_WARNING = ':confused_parrot: Podaj numer zadania w Jirze np. 3242 :confused_parrot:'

jira_app = Blueprint('jira_app', __name__)

@jira_app.route('/jira', methods=['POST'])
@requires_auth
def get_jira_link():
    jira_task_number = get_entered_text()
    if is_number_correct(jira_task_number):
        return jsonify(
            text=get_jira_url(jira_task_number),
            response_type="in_channel"
            )
    else:
        return JIRA_WARNING

def get_jira_url(task_number):
    return JIRA_BASE_URL % task_number

def is_number_correct(jira_task_number):
    return re.match("^[0-9]{4}$", jira_task_number)
