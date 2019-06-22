from flask import Blueprint
from app import db

question = Blueprint('question', __name__)

@question.route('/question/create/<newquestion>')
    def ask(newquestion):
        