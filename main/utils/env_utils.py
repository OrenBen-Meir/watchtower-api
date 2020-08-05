import os


def is_development_env():
    return os.environ.get('FLASK_ENV') == 'development'


def is_staging_env():
    return os.environ.get('FLASK_ENV') == 'staging'


def is_production_env():
    return not (is_development_env() or is_staging_env())
