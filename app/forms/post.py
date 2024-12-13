from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import StringField, SubmitField


class ChooseThemeForm(FlaskForm):
    professor = SelectField("Преподаватель", render_kw={'class': 'form-control', "autocomplete": "off"})
    subject = StringField("Тема", render_kw={'class': 'form-control'})
    submit = SubmitField("Отправить", render_kw={'class': 'btn btn-success'})
