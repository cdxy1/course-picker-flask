from app.extensions import db


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    subject = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(200), nullable=False)