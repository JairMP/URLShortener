from flask import Response
from flask_restful import Resource
from flask import request
from controllers.url_original import to_original_url
from flask import request

from controllers.url_shortener import to_short_url


class Url_Shortener(Resource):

    def get(self):
        return to_original_url(request.args.get('url'))

    def post(self) -> dict:
        return to_short_url(request.get_json())
