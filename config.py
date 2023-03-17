from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from constants import DATA_BASE_URL
from routes.urls_blueprint import url_shortener_bp


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATA_BASE_URL
db = SQLAlchemy(app)
from models import *  # nopep8

migrate = Migrate(app, db)

Api(app)

app.register_blueprint(url_shortener_bp)
