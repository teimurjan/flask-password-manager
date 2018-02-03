from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config
from app.controllers import create_controllers
from app.models import create_models
from flask_login import LoginManager
from flask_migrate import Migrate


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    db = SQLAlchemy()
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    create_controllers(app)

    migrate = Migrate(app, db)
    create_models(db, login_manager)
    return app
