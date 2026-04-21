from flask_restx import Namespace, Resource, fields

from src import Letter
from src.models.word import Word
from src.ext import api

ns_words = Namespace("words", path="/api")

words_model = api.model("Words", {
    "id": fields.Integer,
    "word": fields.String,
    "image": fields.String,
    "sound": fields.String,
    "round_id": fields.Integer,})


@ns_words.route("/words")
class WordListAPI(Resource):
    @ns_words.marshal_with(words_model)
    def get(self):
        words = Word.query.all()
        return words

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

@ns_words.route("/words/<int:id>")
class WordAPI(Resource):
    @ns_words.marshal_with(word_with_letters_model)
    def get(self, id):
        word = Word.query.get(id)
        letters = [
            Letter.query.filter(Letter.letter == l).first()
            for l in word.word
        ]
        word.letters = letters
        return word