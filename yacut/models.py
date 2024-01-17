from datetime import datetime

from flask import url_for

from yacut import db


class URLMap(db.Model):
    """
    The model works with original and short links.
    """
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(250))
    short = db.Column(db.String(16))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """
        Converting an object into a dictionary.
        """
        return dict(
            url=self.original,
            short_link=url_for('redirect_view', short=self.short, _external=True),
        )
