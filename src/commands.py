from flask.cli import with_appcontext
import click
from src.ext import db

def init_db():
    click.echo("Initializing database...")
    db.drop_all()
    db.create_all()
    click.echo("Database created!")

def populate_db():
    click.echo("Populating database...")
    # User
    click.echo("Done!")

@click.command("init_db")
@with_appcontext
def init_db_command():
    init_db()

@click.command("populate_db")
@with_appcontext
def populate_db_command():
    populate_db()