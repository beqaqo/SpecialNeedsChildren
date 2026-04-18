from src.ext import db

class Round(db.Model):
    __tablename__ = "rounds"

    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.Integer, nullable=False)
    next_word_id = db.Column(db.Integer, db.ForeignKey("words.id", use_alter=True, name="fk_round_next_word"), nullable=True)

    words = db.relationship("Word", back_populates="round", foreign_keys="Word.round_id")