from flask import Response, json
from flask_restful import Resource
from flask import request
from constants import BASE_URL, HTTP, HTTPS
from controllers.url_original import to_original_url
from flask import request
from marshmallow import ValidationError

from controllers.url_shortener import to_short_url
from validators.url_validator import UrlPayloadSchema


class Url_Shortener(Resource):
    def get(self):
        url = request.args.get("url")

        if not url:
            return Response(
                response=json.dumps({"error": "url parameter is required"}), status=400
            )

        if HTTP in url or HTTPS in url:
            return Response(
                response=json.dumps({"error": "url cant contains http:// or https://"}),
                status=400,
            )

        if not BASE_URL in url:
            return Response(response=json.dumps({"error": "not valid URL"}), status=400)

        return to_original_url(url.replace("www.short.com/", ""))

    def post(self) -> dict:
        try:
            url = UrlPayloadSchema().load(request.get_json())
        except ValidationError as err:
            return Response(response=json.dumps({"errors": err.messages}), status=400)

        return to_short_url(url)
