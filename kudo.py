import requests
from flask import Blueprint, Response, request, json
from common import requires_auth
from message import get_entered_text

kudo_app = Blueprint('kudo_app', __name__)


@kudo_app.route('/kudo', methods=['POST'])
@requires_auth
def send_kudo():
    headers = {'content-type': 'application/json'}
    url = request.form.get('response_url')
    user = get_entered_text().split(' ', 1)[0]
    reason = get_entered_text().split(' ', 1)[1]

    data = {
        "attachments": [
            {"color": "#439FE0",
             "text": "Nowe kudo! \n:star2: %s :star2:\n*%s*" % (user, reason),
             "mrkdwn_in": ["text"]}], "response_type": "in_channel", "parse": "full", "link_names": 1}

    requests.post(url, data=json.dumps(data), headers=headers)
    return Response(), 200
