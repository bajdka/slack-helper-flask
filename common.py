# -*- coding: utf-8 -*-
import os
from functools import wraps
from flask import request, Response

DEBUG = False

SLACK_WEBHOOK_SECRET = os.environ['SLACK_WEBHOOK_SECRET']

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not is_authorized():
            return Response(), 401
        return f(*args, **kwargs)
    return decorated

def is_authorized():
    if DEBUG:
        return True
    else:
        return request.form.get('token') == SLACK_WEBHOOK_SECRET

def get_entered_text():
    return request.form.get('text').lower()
