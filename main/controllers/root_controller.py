from flask import (url_for, flash, redirect, request, abort, Blueprint, jsonify)
from main.application import db

root_bp = Blueprint('root_bp', __name__)


@root_bp.route("/")
def rootRoute():
    return "watchtower"
