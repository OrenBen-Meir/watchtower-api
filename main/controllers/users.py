from flask import url_for, flash, redirect, request, abort, Blueprint, jsonify
from flask_login import login_user, current_user, logout_user, login_required
from main.errors import error_creation
from main.utils.request_utils import request_is_json
from main.layouts.users import UserLayout
from main.services import user_service

users_bp = Blueprint('users_bp', __name__, url_prefix="/users")

@users_bp.route("/register", methods=['POST'])
@request_is_json
def register():
    if current_user.is_authenticated:
        raise error_creation.bad_request(reasons=["you can't register when authenticated"])
    user_layout = UserLayout().from_dict(request.json)

    response_layout = user_service.register_user(user_layout)
    return jsonify(response_layout.to_dict())

@users_bp.route('/login', methods=[ 'POST'])
@request_is_json
def login():
    #todo: impliment it
    return jsonify({})

@users_bp.route("/", methods=['GET'])
def test():
    # just a dummy route, will either be deleted or modified
    return "hello"
