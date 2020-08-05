from flask import Blueprint, send_from_directory, jsonify

from main.errors import error_creation
from main.utils.env_utils import is_production_env

root_blueprint = Blueprint('root_bp', __name__)


# set up support for static file support
@root_blueprint.route('/static/<path:path>')
def send_static(path):
    production_blocked_paths = ["swagger.yml"]
    if is_production_env() and path in production_blocked_paths:
        error_creation.not_found()
    return send_from_directory('static', path)


@root_blueprint.route("/")
def rootRoute():
    return jsonify(app="watchtower")
