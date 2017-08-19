from flask import jsonify, request

def send_slack_message(method):
    return jsonify(
        text=method,
        response_type="in_channel"
    )

def get_entered_text():
    return request.form.get('text').lower()
