import datetime
from flask import request
from requests import HTTPError

from main.application import firebase
from main.errors import error_creation
from main.models.user_model import UserQuery
from main.security import cookie_names
from main.security.crypt import aes_encrypt, aes_decrypt
from main.errors.error_handler import value_to_server_error

"""
A library dedicated to managing user sessions and retrieving user info.
The functions here fall in the security package as user information is generally
sensitive and thus must be done within a security context.
"""


@value_to_server_error
def user_session_token_encrypt(token: str):
    """
    returns an encrypted jwt token
    """
    return aes_encrypt(token)


@value_to_server_error
def decrypt_session_cookie_to_token(session_cookie: str):
    """
    return a decrypted session cookie as a jwt token
    """
    return aes_decrypt(session_cookie)


def set_session_cookie_from_token(response, token):
    """
    Takes a response object and token, encrypts the token,
    and creates a session cookie
    """
    expires_in = datetime.timedelta(days=5)
    expires = datetime.datetime.now() + expires_in
    response.set_cookie(
        cookie_names.session,
        value=user_session_token_encrypt(token),
        httponly=True,
        expires=expires
    )


def get_session_cookie():
    """
    Returns the session cookie. It is expected that the cookie is encrypted if said session cookie exists
    """
    return request.cookies.get(cookie_names.session)


def clear_session_cookie(response):
    """
    clears session cookie of response
    """
    response.set_cookie(cookie_names.session, '', expires=0)


def get_session_user_data():
    """
    Returns a None if user not signed in,
    otherwise returns a dictionary of user info from your session of this form:

    {
        "localId": "your firebase uid (user id)",
        "email": "example@email.com",
        "username": "exampleName"
        "passwordHash": "ASDFGHJKL=",
        "emailVerified": True,
        "user_roles" = ["manager", "admin"]
        "passwordUpdatedAt": 1595719872845,
        "providerUserInfo": [
            {
                "providerId": "password",
                "federatedId": "example@email.com",
                "email": "example@email.com",
                "rawId": "example@email.com"
            }
        ],
      "validSince": "1595719872",
      "lastLoginAt": "1595719872845",
      "createdAt": "1595719872845",
      "lastRefreshAt": "2020-07-25T23:31:12.845Z",
      "idToken": "someIdTokenForLoggedInUser"
    }
    """
    session_cookie = get_session_cookie()
    if session_cookie is None:
        return None
    token = decrypt_session_cookie_to_token(session_cookie)
    auth = firebase.auth()
    try:
        account_info = auth.get_account_info(token)
        user_data: dict = account_info['users'][0]
    except HTTPError:
        return None
    except KeyError:
        raise error_creation.server_error()
    except IndexError:
        raise error_creation.server_error()
    user = UserQuery.get_first_active_user_with_firebase_uid(user_data['localId'])
    user_data['username'] = user.username
    user_data["user_roles"] = user.user_roles_list
    user_data["idToken"] = token
    return user_data
