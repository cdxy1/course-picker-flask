from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required

from app.extensions import db
from app.models.post import Post
from app.models.user import User
from app.models.user import UserRole
from app.models.forms import ChooseThemeForm

post = Blueprint("post", __name__)


@post.route("/post/choose_theme", methods=["GET", "POST"])
@login_required
def choose_theme():
    form = ChooseThemeForm()
    user = User.query.filter_by(id=current_user.get_id()).first()
    form.professor.choices = [professor.name for professor in User.query.filter_by(role=UserRole.PROFESSOR).all()]
    if UserRole.STUDENT == user.role:
        if form.validate_on_submit():
            pass
        else:
            print(type(current_user.role))
            return render_template("post/choose_theme.html", form=form)
    else:
        return redirect(url_for("main.index"))
