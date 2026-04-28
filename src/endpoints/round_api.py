from flask_restx import Namespace, Resource, fields
from src.models import Round, Letter
from src.ext import api

ns_rounds = Namespace("rounds", path = '/api')

rounds_model = api.model(
    "Rounds",
    {"id": fields.Integer, "position": fields.Integer, "image": fields.String,})

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


round_with_words_model = api.model("WordWithLetters", {
    "id": fields.Integer,
    "image": fields.String,
    "words": fields.List(fields.Nested(word_with_letters_model)),
})

@ns_rounds.route("/rounds")
class RoundListAPI(Resource):
    @ns_rounds.marshal_with(rounds_model)
    def get(self):
        rounds = Round.query.all()
        for round in rounds:
            for word in round.words:
                letters = [
                    Letter.query.filter(Letter.letter == l).first()
                    for l in word.word
                ]
                word.letters = letters
        return rounds

@ns_rounds.route("/rounds/<int:id>")
class RoundAPI(Resource):
    @ns_rounds.marshal_with(round_with_words_model)
    def get(self, id):
        round = Round.query.get_or_404(id)
        for word in round.words:
            letters = [
                    Letter.query.filter(Letter.letter == l).first()
                    for l in word.word
                ]
            word.letters = letters

        return round