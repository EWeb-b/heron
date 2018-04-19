from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.json_encoder import AlchemyEncoder

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
app.json_encoder = AlchemyEncoder
# migrate = Migrate(app, db)

from app import views, models, api
