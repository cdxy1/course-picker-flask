from enum import Enum

from ..extensions import db


class UserRole(Enum):
    STUDENT = "Student"
    PROFESSOR = "Professor"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    # role = db.Column(db.Enum(UserRole), nullable=True)
