from os import path

class Config(object):

    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SECRET_KEY = 'AWDWQDASDSAFHSFJWIasjdalskfjqwoijf@1234098'

    BASE_DIRECTORY = path.abspath(path.dirname(__file__))
