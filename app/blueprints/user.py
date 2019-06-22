from flask import Blueprint
from app.models import User
from app import db

session = db.session

user = Blueprint('user', __name__)


@user.route('/user')
def username():
    all_users = User.query.all()
    print(all_users)
    returnString = ""

    for user in all_users:
        returnString += "User %s ID %d " % (user.username, user.id)

    return returnString


@user.route('/user/<username>')
def user_specific(username):
    a_user = User.query.filter_by(username=username).first_or_404()

    returnString = "User %s ID %d" % (a_user.username, a_user.id)

    return returnString


@user.route('/user/create/<username>')
def createuser(username):
    newUser = User(username=username)
    session.add(newUser)
    session.commit()
    return newUser.username
