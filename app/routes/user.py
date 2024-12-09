from flask import Blueprint, render_template, redirect, flash, request

from app.extensions import bcrypt, db
from app.functions import save_image
from app.models.forms import RegistrationForm, LoginForm
from app.models.user import User, UserRole

user = Blueprint("user", __name__)


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
        except Exception as e:
            db.session.rollback()
            return redirect("https://www.google.ru/")
    else:
        return render_template("user/register.html", objects=[e.value for e in UserRole], form=form)


@user.route("/user/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("user/login.html", form=form)
