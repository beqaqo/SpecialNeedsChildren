from src.ext import db

class Round(db.Model):
    __tablename__ = "rounds"

    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(64), nullable=True)

    words = db.relationship("Word", back_populates="round", foreign_keys="Word.round_id")

    def __repr__(self):
        return f"Round {self.position}"