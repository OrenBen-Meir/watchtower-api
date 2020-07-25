from functools import wraps
from flask import request

from main.errors import error_creation


def request_is_json(function):
    """
    decorator to ensure request is a json
    """

    @wraps(function)
    def wrapper():
        if not request.json:
            raise error_creation.bad_request(reasons=["not json"])
        return function()

    return wrapper


def success_response(message="Success!!") -> dict:
    """
    generic success json response dictionary
    """
    return {"success_message": message}


