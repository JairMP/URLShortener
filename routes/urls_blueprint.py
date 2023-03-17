from flask import Blueprint
from flask_restful import Api

from routes.url_shortener_routes import Url_Shortener

url_shortener_bp = Blueprint("url_shortener_bp", __name__, url_prefix="/url/shortener")

api = Api(url_shortener_bp)

api.add_resource(Url_Shortener, "/", strict_slashes=False)
