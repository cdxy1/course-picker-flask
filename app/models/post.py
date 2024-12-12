from datetime import datetime

from app.extensions import db


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    subject = db.Column(db.String(), nullable=False)
    professor_name = db.Column(db.String(200), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    student_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
