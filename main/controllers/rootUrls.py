from flask import (url_for, flash, redirect, request, abort, Blueprint, jsonify)
from main.application import db

root = Blueprint('root', __name__)

@root.route("/")
def testRoute():
    return jsonify(test="root", variable=-1)