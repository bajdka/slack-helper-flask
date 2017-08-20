import sys
from flask import jsonify, request


def send_slack_message(message):
    try:
        return jsonify(
            text=message,
            response_type="in_channel"
        )
    except:
        return sys.exc_info()[0]


def get_entered_text():
    return request.form.get('text').lower()
