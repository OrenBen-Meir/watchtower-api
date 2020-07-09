import os

class Config:
    """
    describes general application configuration, mainly from the environment
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False                                  # prevents SQL alchemy FSADeprecationWarning warning
    SEND_FILE_MAX_AGE_DEFAULT = 0                                           # to prevent caching
    FLASK_ENV = os.environ.get('FLASK_ENV')
    CLOUDINARY_CLOUD_NAME = os.environ.get('CLOUDINARY_CLOUD_NAME')
    CLOUDINARY_API_KEY = os.environ.get('CLOUDINARY_API_KEY')
    CLOUDINARY_API_SECRET = os.environ.get('CLOUDINARY_API_SECRET')
    SECRET_KEY = os.environ.get('SECRET_KEY')                               
    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{os.environ.get('SQL_USERNAME')}:{os.environ.get('SQL_PASSWORD')}"
        f"@{os.environ.get('SQL_SERVER_NAME')}/watchtower?"
        f"driver={os.environ.get('SQL_DRIVER')}"
    )

    # Todo: set the email configs below to handle any mail client for user
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')                
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')           