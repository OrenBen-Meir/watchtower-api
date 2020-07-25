from functools import wraps
from flask import request
from flask_sqlalchemy import Pagination

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


def success_response() -> dict:
    """
    generic success json response dictionary
    """
    return {"success": True}


def pagination_to_dict(page: Pagination) -> dict:
    if page.per_page > page.total:
        per_page = page.total
    else:
        per_page = page.per_page
    return {
        'items': page.items,
        'page': page.page,
        'per_page': per_page,
        'total': page.total
    }
