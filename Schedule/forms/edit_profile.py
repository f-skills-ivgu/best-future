from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class EditProfile(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    note = StringField('Группа', validators=[DataRequired()])
    submit = SubmitField('Изменить')
