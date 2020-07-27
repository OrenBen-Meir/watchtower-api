from requests import HTTPError

from main.application import firebase, db
from main.business_rules import user_rules
from main.errors import error_reasons, error_creation
from main.layouts.user_layouts import UserLoginLayout, UserSignUpLayout, UserInfoLayout
from main.models.user_model import UserQuery, User
from main.security import roles, session
from main.utils.data_format import pagination_to_dict


def register_user(user_signup_layout: UserSignUpLayout) -> (UserInfoLayout, str):
    """
    takes in registration info from user_signup_layout and registers a user.
    returns a tuple of the form (user_info_layout, a user token)
    """
    user_rules.user_creation_rules(user_signup_layout)
    auth = firebase.auth()
    try:
        firebase_user = auth.create_user_with_email_and_password(user_signup_layout.email, user_signup_layout.password)
    except HTTPError:
        raise error_creation.bad_request(reasons=["Account already exists"])
    if UserQuery.exists_active_user_with_firebase_uid(firebase_user['localId']):
        UserQuery.active_users_with_firebase_uid(firebase_user['localId']).update(dict(active=False))
    user_row = User(username=user_signup_layout.username, firebase_uid=firebase_user['localId'])
    user_row.user_roles_list = [roles.regular]
    db.session.add(user_row)
    db.session.commit()
    id_token: str = firebase_user['idToken']
    auth.send_email_verification(id_token)
    user_info_layout = UserInfoLayout(username=user_signup_layout.username, email=user_signup_layout.email, user_roles=user_row.user_roles_list)
    return user_info_layout, id_token


def login_from_layout(login_user_layout: UserLoginLayout) -> (UserInfoLayout, str):
    """
        takes in login info from login_user_layout and logs in a user by generating a token.
        returns a tuple of the form (user_info_layout, a user token). The token may then be processed into
        a session cookie.
    """
    auth = firebase()
    try:
        user_data = auth.sign_in_with_email_and_password(login_user_layout.email, login_user_layout.password)
    except HTTPError:
        raise error_creation.bad_request(reasons=[error_reasons.bad_request_invalid_credentials()])
    user = UserQuery.get_first_active_user_with_firebase_uid(user_data['localId'])
    token: str = user_data['idToken']
    return UserInfoLayout(username=user.username, email=user_data['email']), token


def logged_in_user() -> UserInfoLayout:
    """
    Returns current user info from session if logged in, otherwise the info is empty.
    """
    user_data = session.get_session_user_data()
    if user_data is None:
        return UserInfoLayout()
    return UserInfoLayout(username=user_data['username'], email=user_data['email'], user_roles=user_data['user_roles'])


def get_users(page: int, per_page: int) -> dict:
    """
    Returns a dictionary of paginated info of users
    """
    users_pagination = UserQuery.get_active_users_by_pagination(page, per_page)
    users_pagination.items = [UserInfoLayout.from_user(user).to_dict() for user in users_pagination.items]
    return pagination_to_dict(users_pagination)
