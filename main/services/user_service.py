from requests import HTTPError

from main.application import firebase, db
from main.business_rules import user_rules
from main.errors import error_reasons, error_creation
from main.schemas.user_schemas import UserLoginSchema, UserSignUpSchema, UserInfoSchema
from main.models.user_model import UserQuery, User
from main.security import roles, session
from main.utils.data_format import pagination_to_dict


def register_user(user_signup_schema: UserSignUpSchema) -> (UserInfoSchema, str):
    """
    takes in registration info from user_signup_schema and registers a user.
    returns a tuple of the form (user_info_schema, a user token)
    """
    user_rules.user_creation_rules(user_signup_schema)
    auth = firebase.auth()
    try:
        firebase_user = auth.create_user_with_email_and_password(user_signup_schema.email, user_signup_schema.password)
    except HTTPError:
        raise error_creation.bad_request(reasons=["Account already exists"])

    session_id_token: str = firebase_user['idToken']
    user_uid: str = firebase_user['localId']

    if UserQuery.exists_active_user_with_firebase_uid(user_uid):
        UserQuery.active_users_with_firebase_uid(user_uid).update(dict(active=False))

    user_row = User(username=user_signup_schema.username, firebase_uid=user_uid)
    user_row.user_roles_list = [roles.regular]
    db.session.add(user_row)
    db.session.commit()

    auth.send_email_verification(session_id_token)
    user_info_schema = UserInfoSchema(
        uid=user_uid,
        username=user_signup_schema.username,
        email=user_signup_schema.email,
        user_roles=user_row.user_roles_list
    )
    return user_info_schema, session_id_token


def login_from_schema(login_user_schema: UserLoginSchema) -> (UserInfoSchema, str):
    """
        takes in login info from login_user_schema and logs in a user by generating a token.
        returns a tuple of the form (user_info_schema, a user token). The token may then be processed into
        a session cookie.
    """
    auth = firebase.auth()
    try:
        user_data = auth.sign_in_with_email_and_password(login_user_schema.email, login_user_schema.password)
    except HTTPError:
        raise error_creation.bad_request(reasons=[error_reasons.bad_request_invalid_credentials()])
    user = UserQuery.get_first_active_user_with_firebase_uid(user_data['localId'])

    user_info_schema = UserInfoSchema(
        uid=user.firebase_uid,
        username=user.username,
        email=user_data['email'],
        user_roles=user.user_roles
    )
    session_token: str = user_data['idToken']
    return user_info_schema, session_token


def logged_in_user() -> UserInfoSchema:
    """
    Returns current user info from session if logged in, otherwise the info is empty.
    """
    user_data = session.get_session_user_data()
    if user_data is None:
        return UserInfoSchema()
    return UserInfoSchema(
        uid=user_data['localId'],
        username=user_data['username'],
        email=user_data['email'],
        user_roles=user_data['user_roles']
    )


def get_users(page: int, per_page: int) -> dict:
    """
    Returns a dictionary of paginated info of users
    """
    users_pagination = UserQuery.get_active_users_by_pagination(page, per_page)
    users_pagination.items = [UserInfoSchema.from_user(user).to_dict() for user in users_pagination.items]
    return pagination_to_dict(users_pagination)
