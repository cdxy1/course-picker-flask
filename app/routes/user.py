from flask import Blueprint

from app.extensions import db
from app.models.user import User

user = Blueprint("user", __name__)


@user.route("/user/<name>/<surname>")
def create_user(name, surname):
    user = User(name=name, surname=surname)
    db.session.add(user)
    db.session.commit()
    return "add"
