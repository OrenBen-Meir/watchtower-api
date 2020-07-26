from functools import wraps
from flask import request

from main.errors import error_creation, error_reasons


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


def get_request_pagination_info() -> (int, int):
    args = request.args
    page, per_page = None, None
    try:
        page = int(args.get("page"))
    except TypeError:
        pass
    except ValueError:
        error_reasons.bad_request_element_must_be_an_integer(args.get("page"))
    try:
        per_page = int(args.get("per_page"))
    except TypeError:
        pass
    except ValueError:
        error_reasons.bad_request_element_must_be_an_integer(args.get("per_page"))
    return page, per_page
