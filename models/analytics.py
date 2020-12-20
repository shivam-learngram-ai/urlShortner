from dataclasses import dataclass
from datetime import datetime as dt

from . import db


@dataclass
class Analytics(db.Model):
    id: int
    url_id: int

    id = db.Column(db.Integer, primary_key=True)
    url_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=dt.utcnow)
