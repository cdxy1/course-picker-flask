from flask import Blueprint, render_template

from app.extensions import db
from app.models.post import Post

post = Blueprint("post", __name__)


@post.route("/post/<subject>/<name>")
def create_post(subject, name):
    post = Post(subject=subject, name=name)
    db.session.add(post)
    db.session.commit()


@post.route("/post/create", methods=["GET", "POST"])
def create():
    return render_template("post/create.html")
