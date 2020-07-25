from main.layouts.users import UserLayout
from main.models.user_model import User
from main.errors.error_creation import bad_request
from validate_email import validate_email


def user_creation_rules(user_layout: UserLayout):
    reasons = []

    if user_layout.username is None:
        reasons.append("Username can't be empty")
    else:
        if User.query.filter_by(username=user_layout.username).count() > 0:
            reasons.append("username already used")
        if len(user_layout.username) < 6 and 30 < len(user_layout.username):
            reasons.append("Username must be 6 to 30 characters")

    if user_layout.email is None:
        reasons.append("email can't be empty")
    else:
        if User.query.filter_by(email=user_layout.email).count() > 0:
            reasons.append("email already used")
        if not validate_email(email_address=user_layout.email, check_regex=True, check_mx=False):
            reasons.append("email not formatted correctly")

    if user_layout.password is None or len(user_layout.password) < 6:
        reasons.append("password must be 6 characters ot more")

    if len(reasons) > 0:
        raise bad_request(reasons=reasons)
