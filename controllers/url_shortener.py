from flask import Response, json
import shortuuid
from constants import BASE_URL, HTTP, HTTPS
from models.url_model import Url, db


def to_short_url(url: dict):
    origina_url = url.get('url')

    if HTTP in origina_url or HTTPS in url:
        return Response(response=json.dumps({'error': "url cant contains http:// or https://"}), status=400)

    short_url = shortuuid.uuid()[:10]

    url = Url(
        hashUrl=short_url,
        originalUrl=url.get('url')
    )

    url.save()

    return Response(response=json.dumps({'message': 'success', 'short_url': f'{BASE_URL}{short_url}'}), status=200)
