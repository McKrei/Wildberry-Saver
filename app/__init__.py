from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static')
app.config.from_object('config.Config')

db = SQLAlchemy(app)

from . import models, views  # noqa

db.create_all()
