from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required

from app.extensions import db
from app.forms.post import ChooseThemeForm
from app.models.post import Post
from app.models.user import User, UserRole

post = Blueprint("post", __name__)


@post.route("/post/choose_theme", methods=["GET", "POST"])
@login_required
def choose_theme():
    form = ChooseThemeForm()
    user = User.query.filter_by(id=current_user.get_id()).first()

    form.professor.choices = [professor.name for professor in User.query.filter_by(role=UserRole.PROFESSOR).all()]
    if UserRole.STUDENT == user.role:

        if form.validate_on_submit():
            post = Post(subject=form.subject.data, professor_name=form.professor.data, student_id=current_user.get_id())
            try:
                db.session.add(post)
                db.session.commit()
                flash("Тема отправлена успешно отправлена", "success")
                return redirect(url_for("user.profile"))
            except:
                db.session.rollback()
                flash("Что-то пошло не так", "danger")
                return redirect(url_for("user.profile"))
        else:
            return render_template("post/choose_theme.html", form=form)
    else:
        return redirect(url_for("main.index"))


@post.route("/post/revision", methods=["GET", "POST"])
@login_required
def revision():
    posts = Post.query.filter_by(professor_name=current_user.name).all()
    if request.method == "POST":

        try:
            post = Post.query.filter_by(subject=request.form["subject"]).first()
            post.grade = request.form["grade"]
            db.session.commit()


            flash("Оценка отправлена", "success")
            return redirect(url_for("user.profile"))
        except Exception as e:
            print(e)
            flash("Произошла ошибка", "danger")
            return redirect(request.url)
    else:
        return render_template("post/revision.html", posts=posts)
