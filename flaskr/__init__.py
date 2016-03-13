from flask import Flask
from flask.ext.sqalchemy import SQLAlchemy

app = Flask(__name__)
app.comfig.from_object('flaskr.config')
db = SQLAlchemy(app)

import flaskr.views
