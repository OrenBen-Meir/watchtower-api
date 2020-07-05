# this is for testing and demonstration, will later be removed
from flask import (render_template, url_for, flash, redirect, request, abort, Blueprint, jsonify)
from main.application import db

testBlueprint = Blueprint('testBlueprint', __name__, url_prefix="/test")

@testBlueprint.route("/")
def testRoute():
    return jsonify(test="sub", variable=4)

@testBlueprint.route("/test2")
def testRoute2():
    return jsonify(test="subsub", variable=5)