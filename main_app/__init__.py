from flask import Flask
from flask_login import LoginManager
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migragte = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from main_app import routes, models
