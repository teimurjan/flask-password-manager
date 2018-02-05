from .auth import auth as auth_blueprint
from .home import home as home_blueprint

def init_blueprints(app):
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(home_blueprint)