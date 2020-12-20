from flask import jsonify


def response(success, message, status_code=200, **kwargs):
    return jsonify({"success": success, "message": message, **kwargs}), status_code


def get_parsed_data_list(request, key_list):
    return [request.json.get(key, None) for key in key_list]
