from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Url(db.Model):
    hashUrl = db.Column(db.String(10), primary_key=True)
    originalUrl = db.Column(db.String(512))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def get_by_hashUrl(hashUrl):
        return Url.query.filter_by(hashUrl=hashUrl).first()
