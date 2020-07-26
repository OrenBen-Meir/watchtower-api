from functools import wraps

from main.errors import error_creation


def value_to_server_error(f):
    """
    decorator which handles value error by raising a server error
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ValueError:
            raise error_creation.server_error()

    return wrapper
