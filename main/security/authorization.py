from functools import wraps

from requests import HTTPError

from main.errors import error_creation, error_reasons
from main.models.user_model import UserQuery
from main.security import session
from main.application import firebase


def authenticate(roles: list = None, check_email_verified: bool = False):
    """
    Decorator that makes sure a user is required to be  authenticated for a request.
    Set roles list to provide a list of user roles that can access a request .
    Set check_email_verified to be True if email must be verified for an action
    """

    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            session_cookie = session.get_session_cookie()
            if session_cookie is None:
                raise error_creation.authorization_error(reasons=[error_reasons.authorization_not_signed_in()])

            token = session.decrypt_session_cookie_to_token(session_cookie)
            auth = firebase.auth()

            try:
                account_info = auth.get_account_info(token)
            except HTTPError:
                raise error_creation.authorization_error(reasons=[error_reasons.authorization_not_signed_in()])

            try:
                uid = account_info['users'][0]['localId']
                email_verified = account_info['users'][0]['emailVerified']
            except KeyError:
                raise error_creation.server_error()
            except IndexError:
                raise error_creation.server_error()

            user = UserQuery.get_first_active_user_with_firebase_uid(uid)
            if user is None:
                raise error_creation.server_error()

            if check_email_verified and not email_verified:
                raise error_creation.authorization_error(reasons=[error_reasons.authorization_email_not_verified()])

            if roles is not None and all(role not in user.user_roles_list for role in roles):
                raise error_creation.permission_error()

            return f(*args, **kwargs)

        return wrapper

    return decorator
