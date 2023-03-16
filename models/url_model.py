from datetime import datetime
from config import db


class Url(db.Model):
    hashUrl = db.Column(db.String(10), primary_key=True)
    originalUrl = db.Column(db.String(512))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
