from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    firstname = db.Column(db.String(64))

    def __init__(self, username, firstname):
        self.username = username
        self.firstname = firstname

    def __repr__(self):
        return '<User %s>' % (self.username)
