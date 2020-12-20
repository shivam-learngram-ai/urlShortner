from flask import redirect

from models.url import Url
from models.analytics import Analytics

from utils import db as db_
from utils.request import response
from utils import base64


def shorten(url, client_id):
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
        short_url=f"http://localhost:5000/url/visit?url={base64.encode(url_object.id)}",
    )


def visit(url):
    url_id = base64.decode(url)
    url_object = Url.query.filter(Url.id == url_id).first()
    if url_object is not None:
        analytics_row = Analytics(url_id=url_object.id)
        db_.add_commit_(analytics_row)
        long_url = url_object.long_url
        if not (long_url.startswith("http://") or long_url.startswith("https://")):
            long_url = f"https://{url_object.long_url}"
        return redirect(long_url, code=307)
    return "Url not Found"


# Analytics


def analytics(url, client_id):
    url_object = (
        Url.query.filter(Url.long_url == url).filter(Url.client_id == client_id).first()
    )
    if url_object is not None:
        analytics_rows = Analytics.query.filter(Analytics.url_id == url_object.id).all()
        return response(
            success=True,
            message="Analytics generated successfully",
            num_hits=len(analytics_rows),
        )
    return response(
        success=True,
        message="This url is not shortened yet",
    )
