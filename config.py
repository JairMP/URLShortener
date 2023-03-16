from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from constants import DATA_BASE_URL


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATA_BASE_URL
db = SQLAlchemy(app)


migrate = Migrate(app, db)

Api(app)
