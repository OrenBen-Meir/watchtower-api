from functools import wraps
from flask import request
from main.errors import error_creation

def request_is_json(function):
    @wraps(function)
    def wrapper():
        if not request.json:
            raise error_creation.bad_request(reasons=["not json"])
        return function()
    return wrapper