from requests import HTTPError

from main.application import firebase, db
from main.business_rules import user_rules
from main.layouts.user_layouts import UserLoginLayout, UserSignUpLayout, UserInfoLayout
from main.models.user_model import UserQuery, User
from main.security import roles
from main.utils.request_utils import success_response
from main.utils.data_format import pagination_to_dict
from main.errors.error_creation import bad_request


def register_user(user_signup_layout: UserSignUpLayout) -> (UserInfoLayout, str):
    user_rules.user_creation_rules(user_signup_layout)
    auth = firebase.auth()
    try:
        firebase_user = auth.create_user_with_email_and_password(user_signup_layout.email, user_signup_layout.password)
    except HTTPError:
        raise bad_request(reasons=["Account already exists"])
    if UserQuery.exists_active_user_with_firebase_uid(firebase_user['localId']):
        UserQuery.active_users_with_firebase_uid(firebase_user['localId']).update(dict(active=False))
    user_row = User(username=user_signup_layout.username, firebase_uid=firebase_user['localId'])
    user_row.user_roles_list = [roles.regular]
    db.session.add(user_row)
    db.session.commit()
    id_token: str = firebase_user['idToken']
    auth.send_email_verification(id_token)
    return UserInfoLayout(username=user_signup_layout.username, email=user_signup_layout.email), id_token


def login_from_layout(login_user_layout: UserLoginLayout) -> dict:
    # Todo: login and return response
    return success_response(message="logged in!!!")


def logged_in_user() -> UserInfoLayout:
    # todo: get your user info
    return UserInfoLayout()


def get_users(page: int, per_page: int) -> dict:
    users_pagination = UserQuery.get_active_users_by_pagination(page, per_page)
    users_pagination.items = [UserInfoLayout.from_user(user).to_dict() for user in users_pagination.items]
    return pagination_to_dict(users_pagination)
