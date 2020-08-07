from flask import request, Blueprint, jsonify

from main.schemas.user_schemas import UserSignUpSchema, UserLoginSchema, UserPasswordResetSchema
from main.security import roles, session
from main.security.authorization import authenticate
from main.services import user_service
from main.utils.request_utils import request_is_json, success_response, get_request_pagination_info

users_api = Blueprint('users_api', __name__, url_prefix="/users")


@users_api.route("/register", methods=['POST'])
@request_is_json
def register():
    user_signup_schema = UserSignUpSchema(json=request.json)
    user_info_schema, token = user_service.register_user(user_signup_schema)
    response = jsonify(user_info_schema.to_dict())
    session.set_session_cookie_from_token(response, token)
    return response


@users_api.route('/login', methods=['POST'])
@request_is_json
def login():
    user_login_schema = UserLoginSchema().from_dict(request.json)
    user_info_schema, token = user_service.login_from_schema(user_login_schema)
    response = jsonify(user_info_schema.to_dict())
    session.set_session_cookie_from_token(response, token)
    return response


@users_api.route('/logout', methods=['GET'])
def logout():
    response = jsonify(success_response(message="logged out!!"))
    session.clear_session_cookie(response)
    return response


@users_api.route('/resetPassword', methods=['POST'])
def reset_password():
    user_password_reset_schema = UserPasswordResetSchema(json=request.json)
    user_service.send_reset_password(user_password_reset_schema)
    return jsonify(success_response(message="Emailed password reset link"))


@users_api.route("/current", methods=['GET'])
@authenticate()
def logged_in_user():
    return jsonify(user_service.logged_in_user().to_dict())


@users_api.route("/userRoles", methods=['GET'])
@authenticate(roles=roles.employees())
def user_roles():
    return jsonify(roles.all_roles())


@users_api.route("/", methods=['GET'])
@authenticate(roles=roles.managers(), check_email_verified=True)
def get_users():
    page, per_page = get_request_pagination_info()
    return jsonify(user_service.get_users(page, per_page))
