import os
from flask_mail import Mail, Message


# Default config for webapp
class Config(object):

    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'Graeme-smells-of-cheese'
    basedir = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # The settings used for emailing the user when a ticket is bought.
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=465
    MAIL_USE_SSL=True
    MAIL_USERNAME='movies.heron@gmail.com'
    MAIL_PASSWORD='Heron111'

# Setup config for testing
class TestConfig(Config):
    DEBUG = True
    Testing = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory'
