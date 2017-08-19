import sys
from flask import jsonify, request


def send_slack_message(method):
    try:
        return jsonify(
            text=method,
            response_type="in_channel"
        )
    except:
        return sys.exc_info()[0]


def get_entered_text():
    return request.form.get('text').lower()
