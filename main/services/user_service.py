from main.business_rules import user_rules
from main.layouts.users import UserLoginLayout, UserSignUpLayout, UserInfoLayout
from main.models.user_model import UserQuery
from main.utils.request_utils import success_response
from main.utils.data_format import pagination_to_dict


def register_user(user_layout: UserSignUpLayout) -> UserInfoLayout:
    # Todo: run user registration
    user_rules.user_creation_rules(user_layout)
    return UserInfoLayout()


def login_from_layout(login_user_layout: UserLoginLayout) -> dict:
    # Todo: login and return response
    return success_response(message="logged in!!!")


def logged_in_user() -> UserInfoLayout:
    # todo: get your user info
    return UserInfoLayout()


def get_users(page: int, per_page: int) -> dict:
    users_pagination = UserQuery.get_active_users_by_pagination(page, per_page)
    users_pagination.items = [UserInfoLayout().from_user(user).to_dict() for user in users_pagination.items]
    return pagination_to_dict(users_pagination)
