from flask import redirect

from models.url import Url

from utils import db as db_
from utils.request import response
from utils import base64


def shorten(url, client_id):
    # url lacking http or https needs to be handled
    url_rows = (
        Url.query.filter(Url.long_url == url).filter(Url.client_id == client_id).all()
    )
    if len(url_rows) > 0:
        url_object = url_rows[0]
    else:
        url_object = Url(long_url=url, client_id=client_id)
        db_.add_commit_(url_object)
    return response(
        success=True,
        message="Your url shortened successfully",
        short_url=base64.encode(url_object.id),
    )


def visit(url):
    url_id = base64.decode(url)
    url_object = Url.query.filter(Url.id == url_id).first()
    print(url_object)
    if url_object is not None:
        return redirect(url_object.long_url, code=307)
    return "Url not Found"
