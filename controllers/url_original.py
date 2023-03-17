from flask import Response, json


def to_original_url(url: str):

    return Response(response=json.dumps({'message': 'success', 'url': f'{url}'}), status=200)
