from flask_login import login_user, current_user

from main.application import db, bcrypt
from main.business_rules import user_rules
from main.errors import error_creation
from main.layouts.users import UserLayout
from main.models.user_model import UserQuery, User
from main.security import roles
from main.utils.request_utils import success_response, pagination_to_dict


def register_user(user_layout: UserLayout) -> UserLayout:
    if current_user.is_authenticated:
        raise error_creation.bad_request(reasons=["you can't register when authenticated"])
    user_layout.id = None
    user_layout.user_roles = [roles.regular]
    user_rules.user_creation_rules(user_layout)

    user = user_layout.to_user(password_encrypted=True)
    db.session.add(user)
    db.session.commit()

    response_layout = UserLayout().from_user(user)
    response_layout.password = None
    return response_layout


def login_from_layout(login_user_layout: UserLayout) -> dict:
    if current_user.is_authenticated:
        raise error_creation.bad_request(reasons=["you can't sign in when authenticated"])
    user = UserQuery.get_user_by_email_or_username(username=login_user_layout.username, email=login_user_layout.email)
    if user and bcrypt.check_password_hash(user.password, login_user_layout.password):
        login_user(user, remember=login_user_layout.remember)
        return success_response()
    else:
        raise error_creation.bad_request(reasons=["login unsuccessful"], success=True)


def logged_in_user() -> UserLayout:
    user_layout = UserLayout().from_user(current_user)
    user_layout.password = None
    return user_layout


def get_users(page: int, per_page: int) -> dict:
    users_pagination = UserQuery.get_users_by_pagination(page, per_page)
    users_pagination.items = [UserLayout().from_user(user, include_password=False).to_dict() for user in
                              users_pagination.items]
    return pagination_to_dict(users_pagination)
