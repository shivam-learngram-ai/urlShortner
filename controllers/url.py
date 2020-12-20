from models.url import Url

from utils import db as db_
from utils.request import response
from utils import base64


def shorten(url, client_id):
    url_object = Url(long_url=url, client_id=client_id)
    db_.add_commit_(url_object)
    return response(
        success=True,
        message="Your url shortened successfully",
        short_url=base64.encode(url_object.id),
    )
