from flask import Blueprint

from app.extensions import db
from app.models.post import Post

post = Blueprint("post", __name__)


@post.route("/post/<subject>/<name>")
def create_post(subject, name):
    post = Post(subject=subject, name=name)
    db.session.add(post)
    db.session.commit()
    return "Post has been added"
