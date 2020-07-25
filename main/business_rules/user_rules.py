from main.layouts.users import UserSignUpLayout
from main.models.user_model import User
from main.errors.error_creation import bad_request
from validate_email import validate_email


def user_creation_rules(user_signup_layout: UserSignUpLayout):
    reasons = []
    # unique email constraint is handled in a service

    if user_signup_layout.username is None:
        reasons.append("Username can't be empty")
    else:
        if User.query.filter_by(username=user_signup_layout.username).count() > 0:
            reasons.append("username already used")
        if len(user_signup_layout.username) < 6 and 30 < len(user_signup_layout.username):
            reasons.append("Username must be 6 to 30 characters")

    if user_signup_layout.email is None:
        reasons.append("email can't be empty")
    else:
        if not validate_email(email_address=user_signup_layout.email, check_regex=True, check_mx=False):
            reasons.append("email not formatted correctly")

    if user_signup_layout.password is None or len(user_signup_layout.password) < 6:
        reasons.append("password must be 6 characters ot more")

    if len(reasons) > 0:
        raise bad_request(reasons=reasons)
