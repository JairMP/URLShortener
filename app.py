from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from constants import DATA_BASE_URL
from models.url_model import db
from routes.urls_blueprint import url_shortener_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATA_BASE_URL
db.init_app(app)

migrate = Migrate(app, db)

Api(app)

app.register_blueprint(url_shortener_bp)

if __name__ == '__main__':
    app.run(debug=True)
