from main.schemas.user_schemas import UserSignUpSchema
from main.models.user_model import User, UserQuery
from main.errors.error_creation import bad_request
from validate_email import validate_email


def user_creation_rules(user_signup_schema: UserSignUpSchema):
    reasons = []

    if user_signup_schema.username is None:
        reasons.append("Username can't be empty")
    else:
        if len(user_signup_schema.username) < 6 or 30 < len(user_signup_schema.username):
            reasons.append("Username must be 6 to 30 characters")
        if UserQuery.exists_active_user_with_username(user_signup_schema.username):
            reasons.append("username already used")

    if user_signup_schema.email is None:
        reasons.append("email can't be empty")
    else:
        if not validate_email(email_address=user_signup_schema.email, check_regex=True, check_mx=False):
            reasons.append("email not formatted correctly")

    if user_signup_schema.password is None or len(user_signup_schema.password) < 6:
        reasons.append("password must be 6 characters or more")

    if len(reasons) > 0:
        raise bad_request(reasons=reasons)
