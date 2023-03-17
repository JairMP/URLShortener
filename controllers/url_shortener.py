from flask import Response, json
import shortuuid
from constants import BASE_URL
from models.url_model import Url, db


def to_short_url(url: dict):
    short_url = shortuuid.uuid()[:10]

    url = Url(
        hashUrl=short_url,
        originalUrl=url.get('url')
    )

    url.save()

    return Response(response=json.dumps({'message': 'success', 'short_url': f'{BASE_URL}{short_url}'}), status=200)
