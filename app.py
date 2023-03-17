from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from constants import DATA_BASE_URL
from models import db
from routes.urls_blueprint import url_shortener_bp


def create_app(database=DATA_BASE_URL):
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = database
    db.init_app(app)

    migrate = Migrate(app, db)

    Api(app)

    app.register_blueprint(url_shortener_bp)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
