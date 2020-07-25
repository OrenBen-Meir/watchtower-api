from flask_login import LoginManager


def setup_login_manager() -> LoginManager:
    login_manager = LoginManager()
    login_manager.login_view = '/users/login'  # setup login url
    login_manager.login_message_category = 'info'
    return login_manager
