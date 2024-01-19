from datetime import datetime

from flask import url_for

from yacut import db
from yacut.variables import LEN_OF_ORIGINAL_LINK, LEN_OF_USER_LINK


class URLMap(db.Model):
    """
    The model works with original and short links.
    """
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(LEN_OF_ORIGINAL_LINK))
    short = db.Column(db.String(LEN_OF_USER_LINK))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """
        Converting an object into a dictionary.
        """
        return dict(
            url=self.original,
            short_link=url_for('redirect_view', short=self.short, _external=True),
        )
