from flask import Flask, jsonify
from main.errors import ApplicationException

def _register_urls(app : Flask):
    from main.controllers.test import testBlueprint
    from main.controllers.rootUrls import root
    from main.controllers.errors import errorurl_blueprint
    
    app.register_blueprint(testBlueprint)
    app.register_blueprint(root)
    app.register_blueprint(errorurl_blueprint)

def setup_requests(app : Flask):
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
    def handle_application_error(error : ApplicationException):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response