from flask_login import current_user
from functools import wraps

from main.errors import error_creation


def authenticate(roles: list = None):
    if roles is None:
        roles = []

    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if not current_user.is_authenticated:
                raise error_creation.authorization_error(["login required"])
            if not roles or all(role in current_user.user_roles_list for role in roles):
                return f(*args, **kwargs)
            else:
                raise error_creation.permission_error(["permission denied"])

        return wrapper

    return decorator
