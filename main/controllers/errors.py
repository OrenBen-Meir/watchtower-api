# this is for testing and demonstration, will later be removed
from flask import (render_template, url_for, flash, redirect, request, abort, Blueprint, jsonify)
from main.application import db
from main.errors import error_creation

errorurl_blueprint = Blueprint('errorurl_blueprint', __name__, url_prefix="/errors")

@errorurl_blueprint.route("/")
def badrequest():
    raise error_creation.bad_request(reason = ["test", "this is for demonstration"])

@errorurl_blueprint.route("/noreason")
def noreason():
    raise error_creation.bad_request()

@errorurl_blueprint.route("/notfound")
def notfound():
    raise error_creation.not_found(info="just testing")

@errorurl_blueprint.route("/servererror")
def servererror():
    raise error_creation.server_error(information="just testing")

@errorurl_blueprint.route("/permissionerror")
def permissionerror():
    raise error_creation.permission_error(myinfo="just testing")
