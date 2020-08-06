from flask_swagger_ui import get_swaggerui_blueprint

SWAGER_URL = '/swagger'
API_URL = '/static/swagger.yml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGER_URL,
    API_URL,
    config={
        'app_name': 'Watchtower API'
    }
)
