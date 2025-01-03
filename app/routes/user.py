from flask import Blueprint, render_template, redirect, flash, request, url_for
from flask_login import login_user, login_required, logout_user, current_user

from app.extensions import bcrypt, db, login
from app.functions import save_image
from app.forms.user import RegistrationForm, LoginForm
from app.models.post import Post
from app.models.user import User, UserRole

user = Blueprint("user", __name__)


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@user.route("/user/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        avatar = save_image(form.avatar.data)
        user = User(name=form.name.data, login=form.login.data, password=hashed_password,
                    avatar=avatar, role=UserRole(form.role.data).name)
        try:
            db.session.add(user)
            db.session.commit()
            flash("Вы успешно зарегистрированы!", "success")
            return redirect("/")
        except Exception:
            db.session.rollback()
            return redirect("https://www.google.ru/")
    else:
        return render_template("user/register.html", objects=[e.value for e in UserRole], form=form)


@user.route("/user/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash("Вы успешно авторизированны!", "success")
            login_user(user, form.remember_me.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("user.profile"))
        else:
            flash("Логин или пароль введен неправильно!", "danger")
    return render_template("user/login.html", form=form)


@user.route("/user/profile")
@login_required
def profile():
    user = current_user
    student_post = Post.query.filter_by(student_id=user.id).all()
    professor_post = Post.query.filter_by(professor_name=user.name).all()

    return render_template("user/profile.html", user=user, student_post=student_post, professor_post=professor_post,
                           UserRole=UserRole)


@user.route("/user/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")


@user.after_request
def after_request(response):
    if response.status_code == 401:
        page = f"{url_for('user.login')}?next={request.url}"
        return redirect(page)
    return response
