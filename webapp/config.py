import os

# Default config for webapp


class Config(object):
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'Graeme-smells-of-cheese'
    basedir = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# Setup config for testing
class TestConfig(Config):
    DEBUG = True
    Testing = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory'
