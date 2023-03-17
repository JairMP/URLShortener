from flask import Response, json
import shortuuid
from constants import BASE_URL


def to_short_url(url: str):
    short_url = shortuuid.uuid()[:10]

    return Response(response=json.dumps({'message': 'success', 'short_url': f'{BASE_URL}{short_url}'}), status=200)
