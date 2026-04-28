from flask_restx import Namespace, Resource, fields
from src.models.round import Round
from src.ext import api

ns_rounds = Namespace("rounds", path = '/api')

rounds_model = api.model(
    "Rounds",
    {"id": fields.Integer, "position": fields.Integer, "image": fields.String,})

words_model = api.model("Words", {
    "id": fields.Integer,
    "word": fields.String,
    "image": fields.String,
    "sound": fields.String,
    "round_id": fields.Integer,})


round_with_words_model = api.model("WordWithLetters", {
    "id": fields.Integer,
    "image": fields.String,
    "words": fields.List(fields.Nested(words_model))
})

@ns_rounds.route("/rounds")
class RoundListAPI(Resource):
    @ns_rounds.marshal_with(rounds_model)
    def get(self):
        rounds = Round.query.all()
        return rounds

@ns_rounds.route("/rounds/<int:id>")
class RoundAPI(Resource):
    @ns_rounds.marshal_with(round_with_words_model)
    def get(self, id):
        round = Round.query.get_or_404(id)
        return round