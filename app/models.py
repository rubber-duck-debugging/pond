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

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    resolved = db.Column(db.Boolean)
    asker = db.Column(db.Integer)
    date_asked = db.Column(db.DateTime, nullable=False)
    date_resolved = db.Column(db.DateTime, nullable=True)

    def __init__(self, text, asker, date_asked, resolved=False, date_resolve=None):
        self.text = text
        self.asker = asker
        self.date_asked = date_asked
        self.resolved = resolved
        self.date_resolved = date_resolved

    def __repr__(self):
        return '<Question %s>' % (self.id)