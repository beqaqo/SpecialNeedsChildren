from flask.cli import with_appcontext
import click
from src.ext import db
from src.models import User, Word, Letter, Round

@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Initializing database...")
    db.drop_all()
    db.create_all()
    click.echo("Database created!")

@click.command("populate_db")
@with_appcontext
def populate_db():
    click.echo("Populating database...")



    # User
    admin = User(username="admin", role="admin")
    admin.set_password("admin123")
    db.session.add(admin)

    # Letters
    georgian_alphabet = [
        "ა", "ბ", "გ", "დ", "ე", "ვ", "ზ", "თ", "ი", "კ", "ლ",
        "მ", "ნ", "ო", "პ", "ჟ", "რ", "ს", "ტ", "უ", "ფ", "ქ",
        "ღ", "ყ", "შ", "ჩ", "ც", "ძ", "წ", "ჭ", "ხ", "ჯ", "ჰ"
    ]
    for char in georgian_alphabet:
        letter = Letter(letter=char)
        db.session.add(letter)

    # Rounds
    round1 = Round(position=1)
    round2 = Round(position=2)
    db.session.add_all([round1, round2])
    db.session.flush()  # ID-ebi rom mivigot

    # Words
    words = [
        Word(word="მაგიდა", position=1, round_id=round1.id),
        Word(word="სკამი", position=2, round_id=round1.id),
        Word(word="კატა", position=1, round_id=round2.id),
        Word(word="ძაღლი", position=2, round_id=round2.id),
    ]
    db.session.add_all(words)
    db.session.commit()

    click.echo("Database populated!")

