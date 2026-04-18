from flask import Blueprint, jsonify
from src.models.word import Word
from src.models.round import Round

api_blueprint = Blueprint("api", __name__, url_prefix="/api")

@api_blueprint.route("/words")
def get_words():
    words = Word.query.all()
    return jsonify([
        {
            "id": w.id,
            "word": w.word,
            "image": w.image,
            "sound": w.sound,
            "round_id": w.round_id
        } for w in words
    ])

@api_blueprint.route("/rounds")
def get_rounds():
    rounds = Round.query.all()
    return jsonify([
        {
            "id": r.id,
            "position": r.position,
            "next_word_id": r.next_word_id
        } for r in rounds
    ])

@api_blueprint.route("/round/<int:id>")
def get_round_words(id):
    round = Round.query.get_or_404(id)
    return jsonify([
        {
            "id": w.id,
            "word": w.word,
            "image": w.image,
            "sound": w.sound
        } for w in round.words
    ])