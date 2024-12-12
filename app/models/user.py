from enum import Enum

from flask_login import UserMixin

from ..extensions import db


class UserRole(Enum):
    STUDENT = "Студент"
    PROFESSOR = "Препод"


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    login = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    avatar = db.Column(db.String(250), nullable=True)
    role = db.Column(db.Enum(UserRole), nullable=False)

    post = db.relationship("Post", backref="student")
