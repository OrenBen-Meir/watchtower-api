import os


class Config:
    """
    describes general application configuration, mainly from the environment
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # prevents SQL alchemy FSADeprecationWarning warning
    SEND_FILE_MAX_AGE_DEFAULT = 0  # to prevent caching
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{os.environ.get('SQL_USERNAME')}:{os.environ.get('SQL_PASSWORD')}"
        f"@{os.environ.get('SQL_SERVER_NAME')}/watchtower?"
        f"driver={os.environ.get('SQL_DRIVER')}"
    )

