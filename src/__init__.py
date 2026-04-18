from flask import Flask
from src.ext import db, migrate, login_manager, admin
from src.config import Config
from src.commands import init_db_command, populate_db_command
from src.models import Word, Round, Letter, User # noqa
from src.admin_views.base import SecureModelView, SecureIndexView
from src.views import auth_blueprint, api_blueprint

COMMANDS = [init_db_command, populate_db_command]
BLUEPRINTS = [auth_blueprint, api_blueprint]

def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)

    admin.__init__(app, name="SpecialNeeds Panel", index_view=SecureIndexView())
    admin.add_view(SecureModelView(User, db.session))

def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)

def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app