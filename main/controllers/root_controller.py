from flask import Blueprint, send_from_directory, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

root_blueprint = Blueprint('root_bp', __name__)

# set up support for static file support
@root_blueprint.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


@root_blueprint.route("/")
def rootRoute():
    return jsonify(app="watchtower")
