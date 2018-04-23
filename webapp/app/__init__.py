from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail, Message
from config import Config
from app.json_encoder import AlchemyEncoder

mail = Mail()
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
app.json_encoder = AlchemyEncoder

from app import views, models, api
