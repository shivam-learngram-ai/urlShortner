from dataclasses import dataclass

from . import db


@dataclass
class Url(db.Model):
    id: int
    long_url: str
    client_id: int

    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(2000))
    client_id = db.Column(db.Integer)
