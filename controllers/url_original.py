from flask import Response, json
from models.url_model import Url
from validators.url_validator import UrlSchema


def to_original_url(url: str):

    record = Url.get_by_hashUrl(hashUrl=url)

    if not record:
        return Response(response=json.dumps({'error': 'Short URL not found'}), status=404)

    original_url = UrlSchema().dump(record)

    return Response(response=json.dumps({'message': 'success', 'url': original_url.get('originalUrl')}), status=200)
