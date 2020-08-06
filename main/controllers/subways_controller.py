from flask import request, Blueprint, jsonify

from main.services import subway_service

subways_api = Blueprint('subways_api', __name__, url_prefix="/subways")


@subways_api.route("/", methods=['GET'])
def get_subways():
    return jsonify(subway_service.get_subways().to_dict())
