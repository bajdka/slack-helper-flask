# -*- coding: utf-8 -*-

from flask import Blueprint

simple_app = Blueprint('simple_app', __name__)
@simple_app.route('/dupa')
def show():
    return "dupa"
