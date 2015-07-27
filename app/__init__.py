from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLAlCHEMY_DATABASE_URI"] = "sqlite:////database.db"
db = SQLAlchemy(app)

import views,models
