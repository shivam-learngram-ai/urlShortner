from flask import request, Blueprint, redirect
from utils.request import response, get_parsed_data_list

from controllers import url as url_controller


bp = Blueprint("user", __name__, url_prefix="/url")


@bp.route("/shorten", methods=["POST"])
def shorten():
    """Shorten a given URL
    ---
    tags:
      - URL
    parameters:
      - in: body
        name: Your URL
        description: Your URL
        schema:
          type: object
          required:
            - url
            - client_id
          properties:
            client_id:
              type: integer
            url:
              type: string
    responses:
      200:
        description: Short url
    """
    return url_controller.shorten(*get_parsed_data_list(request, ["url", "client_id"]))


@bp.route("/visit", methods=["GET"])
def progress():
    """Redirects to the long url given a short url
    ---
    tags:
      - URL
    parameters:
      - in: body
        name: Your short URL
        description: Your short URL
        schema:
          type: object
          required:
            - url
          properties:
            url:
              type: string
    responses:
      307:
        description: Short url
    """
    return redirect("http://www.example.com", code=307)
