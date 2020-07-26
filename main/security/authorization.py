from functools import wraps


def authenticate(roles: list = None, verified=True):
    if roles is None:
        roles = []

    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            # Todo: make sure user is signed in
            # Todo: set up roles rules based on firebase
            return f(*args, **kwargs)

        return wrapper

    return decorator
