from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.json_encoder import AlchemyEncoder
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
app.json_encoder = AlchemyEncoder
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)

from app import views, models, api
