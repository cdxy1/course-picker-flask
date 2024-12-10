from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import StringField, PasswordField, SubmitField, FileField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Optional, ValidationError, Regexp, Length

from app.models.user import UserRole, User


class RegistrationForm(FlaskForm):
    name = StringField('ФИО',
                       validators=[DataRequired(), Length(min=2, max=150, message="Слишком длинное или короткое ФИО"),
                                   Regexp('[A-Za-zА-Яа-яЁё]+', message="ФИО должно состоять из букв.")],
                       render_kw={'class': 'form-control', "placeholder": "ФИО"})

    login = StringField("Логин", validators=[DataRequired(), Regexp('[0-9A-Za-z_]+',
                                                                    message="В логине должны быть только латинские буквы и цифры без пробелов и специальных символов"),
                                             Length(min=2, max=20)],
                        render_kw={'class': 'form-control', "placeholder": "Логин"})

    role = SelectField("Роль", validators=[DataRequired()], choices=[role.value for role in UserRole],
                       render_kw={'class': 'form-control'})

    password = PasswordField('Пароль ', validators=[DataRequired(), Length(min=2, max=20,
                                                                           message="Пароль короче 2 или длинее 20 символов")],
                             render_kw={'class': 'form-control', "placeholder": "Пароль"})

    confirm_password = PasswordField('Подтверждение пароля', validators=[DataRequired(),
                                                                         EqualTo('password',
                                                                                 "Пароли должны соответствовать")],
                                     render_kw={'class': 'form-control', "placeholder": "Подтверждение пароля"})

    avatar = FileField("Загрузить фото", validators=[Optional(), FileAllowed(['jpg', 'png', 'jpeg'])],
                       render_kw={'class': 'form-control'})

    submit = SubmitField("Зарегистрироваться", render_kw={'class': 'btn btn-success'})

    def validate_login(self, field):
        if User.query.filter_by(login=field.data).first():
            raise ValidationError("Логин уже занят.")
        elif " " in field.data:
            raise ValidationError("В логине не должно быть пробелов.")
        elif not field.data[0].isalpha():
            raise ValidationError("Логин должен начинаться с буквы.")


class LoginForm(FlaskForm):
    login = StringField("Логин", render_kw={'class': 'form-control', "placeholder": "Логин"})
    password = PasswordField("Пароль", render_kw={'class': 'form-control', "placeholder": "Пароль"})
    remember_me = BooleanField("Запомнить меня", render_kw={'class': 'btn btn-secondary'})
    submit = SubmitField("Войти", render_kw={'class': 'btn btn-success'})

