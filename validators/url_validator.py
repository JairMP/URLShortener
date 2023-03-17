from marshmallow import Schema, fields, validate


class UrlPayloadSchema(Schema):
    url = fields.String()


class UrlSchema(Schema):
    hashUrl = fields.Str()
    originalUrl = fields.Str()
    created_at = fields.DateTime()
