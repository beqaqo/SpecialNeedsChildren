from src.ext import db

class Word(db.Model):
    __tablename__ = "words"

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(255), nullable=True)
    sound = db.Column(db.String(255), nullable=True)
    position = db.Column(db.Integer, nullable=False)
    round_id = db.Column(db.Integer, db.ForeignKey("rounds.id"), nullable=True)

    round = db.relationship("Round", back_populates="words", foreign_keys=[round_id])

    def __repr__(self):
        return self.word