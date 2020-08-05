from main.schemas.user_schemas import UserSignUpSchema
from main.models.user_model import User, UserQuery
from main.errors.error_creation import bad_request
from validate_email import validate_email


def user_creation_rules(user_signup_layout: UserSignUpSchema):
    reasons = []

    if user_signup_layout.username is None:
        reasons.append("Username can't be empty")
    else:
        if 6 > len(user_signup_layout.username) > 30:
            reasons.append("Username must be 6 to 30 characters")
        if UserQuery.exists_active_user_with_username(user_signup_layout.username):
            reasons.append("username already used")

    if user_signup_layout.email is None:
        reasons.append("email can't be empty")
    else:
        if not validate_email(email_address=user_signup_layout.email, check_regex=True, check_mx=False):
            reasons.append("email not formatted correctly")

    if user_signup_layout.password is None or len(user_signup_layout.password) < 6:
        reasons.append("password must be 6 characters ot more")

    if len(reasons) > 0:
        raise bad_request(reasons=reasons)
