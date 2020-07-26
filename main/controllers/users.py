from flask import request, Blueprint, jsonify

from main.errors import error_creation
from main.layouts.user import UserSignUpLayout, UserLoginLayout
from main.security import roles, cookie_names
from main.security.authorization import authenticate
from main.services import user_service
from main.utils.request_utils import request_is_json, success_response

users_bp = Blueprint('users_bp', __name__, url_prefix="/users")


@users_bp.route("/register", methods=['POST'])
@request_is_json
def register():
    user_signup_layout = UserSignUpLayout(json=request.json)
    response_layout, token = user_service.register_user(user_signup_layout)
    res = jsonify(response_layout.to_dict())
    res.set_cookie(cookie_names.session, value=token, httponly=True)
    return res


@users_bp.route('/login', methods=['POST'])
@request_is_json
def login():
    user_layout = UserLoginLayout().from_dict(request.json)
    result = user_service.login_from_layout(user_layout)
    return jsonify(result)


@users_bp.route('/logout', methods=['GET'])
def logout():
    # Todo: clear user session cookie
    return jsonify(success_response(message="logged out!!"))


@users_bp.route("/current", methods=['GET'])
@authenticate()
def logged_in_user():
    return jsonify(user_service.logged_in_user().to_dict())


@users_bp.route("/", methods=['GET'])
@authenticate(roles=[roles.manager, roles.admin])
def get_users():
    args = request.args
    converted_args = {}
    for k in args:
        try:
            if args[k] is None:
                converted_args[k] = int(args.get(k))
        except ValueError:
            raise error_creation.bad_request([f"{k} must be an integer"])
    return jsonify(user_service.get_users(converted_args.get('page'), converted_args.get('per_page')))
