from flask import Flask
from src.ext import db, migrate, login_manager, admin, api
from src.config import Config
from src.commands import init_db, populate_db
from src.models import Word, Round, Letter, User
from src.admin_views.base import SecureModelView, SecureIndexView
from src.views.auth import auth_blueprint
from src.endpoints import ns_rounds, ns_words
from src.admin_views.round_view import RoundView
from src.admin_views.word_view import WordView
from src.admin_views.letter_view import LetterView

COMMANDS = [init_db, populate_db]
BLUEPRINTS = [auth_blueprint]

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app

def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)

    admin.init_app(app, index_view=SecureIndexView())
    admin.add_view(SecureModelView(User, db.session))
    admin.add_view(WordView(Word, db.session))
    admin.add_view(RoundView(Round, db.session))
    admin.add_view(LetterView(Letter, db.session))

    api.init_app(app)
    api.add_namespace(ns_rounds)
    api.add_namespace(ns_words)


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)
