from flask import Flask, jsonify
from main.errors import ApplicationException
from main.utils.env_utils import is_production_env


def _register_urls(app: Flask):
    from main.controllers.root_controller import root_blueprint
    app.register_blueprint(root_blueprint)

    if not is_production_env():
        from main.controllers.swagger_controller import swaggerui_blueprint, SWAGER_URL
        app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGER_URL)

    from main.controllers.users_controller import users_api
    app.register_blueprint(users_api)


def setup_requests(app: Flask):
    """
    configures all http requests.
    must be called last when app is created to prevent circular imports
    """
    _register_urls(app)

    @app.after_request
    def add_header(r):
        """
        Add headers to both force latest IE rendering engine or Chrome Frame,
        and also to cache the rendered page for 10 minutes.
        """
        r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        r.headers["Pragma"] = "no-cache"
        r.headers["Expires"] = "0"
        r.headers['Cache-Control'] = 'public, max-age=0'
        return r

    @app.errorhandler(ApplicationException)
    def handle_application_error(error: ApplicationException):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response
