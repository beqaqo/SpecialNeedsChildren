from src.ext import db

class Letter(db.Model):
    __tablename__ = "letters"

    id = db.Column(db.Integer, primary_key=True)
    letter = db.Column(db.String(5), nullable=False, unique=True)
    image = db.Column(db.String(255), nullable=True)
    sound = db.Column(db.String(255), nullable=True)