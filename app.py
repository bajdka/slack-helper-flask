# -*- coding: utf-8 -*-

from flask import Flask
from claims import claim_app
from contract import contract_app
from jira import jira_app
from kudo import kudo_app
from gui import gui_app
from e2e import e2e_app
from sit import sit_app

app = Flask(__name__)
app.register_blueprint(claim_app)
app.register_blueprint(contract_app)
app.register_blueprint(jira_app)
app.register_blueprint(kudo_app)
app.register_blueprint(gui_app)
app.register_blueprint(e2e_app)
app.register_blueprint(sit_app)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
