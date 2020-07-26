import datetime
from flask import request

from main.security import cookie_names
from main.security.crypt import aes_encrypt, aes_decrypt
from main.errors.error_handler import value_to_server_error


@value_to_server_error
def user_session_token_encrypt(token: str):
    """
    returns an encrypted jwt token
    """
    return aes_encrypt(token)


@value_to_server_error
def decrypt_session_cookie(session_cookie: str):
    """
    return a decrypted session cookie as a jwt token
    """
    return aes_decrypt(session_cookie)


def set_session_cookie(response, token):
    expires_in = datetime.timedelta(days=5)
    expires = datetime.datetime.now() + expires_in
    response.set_cookie(
        cookie_names.session,
        value=user_session_token_encrypt(token),
        httponly=True,
        expires=expires
    )


def get_session_cookie():
    return request.cookies.get(cookie_names.session)
