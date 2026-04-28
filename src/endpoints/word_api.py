from flask_restx import Namespace, Resource, fields

from src.models import Word, Letter
from src.ext import api

ns_words = Namespace("words", path="/api")

letter_model = api.model("Letter", {
    "id": fields.Integer,
    "letter": fields.String,
    "image": fields.String,
    "sound": fields.String,
})

word_with_letters_model = api.model("WordWithLetters", {
    "id": fields.Integer,
    "word": fields.String,
    "image": fields.String,
    "sound": fields.String,
    "round_id": fields.Integer,
    "letters": fields.List(fields.Nested(letter_model))
})


@ns_words.route("/words")
class WordListAPI(Resource):
    @ns_words.marshal_with(word_with_letters_model)
    def get(self):
        words = Word.query.all()
        for word in words:
            letters = [
                Letter.query.filter(Letter.letter == l).first()
                for l in word.word
            ]
            word.letters = letters
        return words
