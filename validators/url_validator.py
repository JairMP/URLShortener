from marshmallow import Schema, fields, validate


class UrlPayloadSchema(Schema):
    url = fields.String(required=True)


class UrlSchema(Schema):
    hashUrl = fields.Str(required=True)
    originalUrl = fields.Str(required=True)
    created_at = fields.DateTime()
