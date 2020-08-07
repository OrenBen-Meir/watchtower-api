"""
error reasons constants and creators
"""


def bad_request_element_must_be_an_integer(k):
    return f"{k} must be an integer"


def bad_request_invalid_credentials():
    return "invalid credentials"


def bad_request_user_not_found():
    return "user not found"


def authorization_email_not_verified():
    return "account email not verified"


def authorization_not_signed_in():
    return "not signed in"
