from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField
from wtforms.validators import DataRequired


class AddLesson(FlaskForm):
    name = StringField('ID предмета', validators=[DataRequired()])
    week_day = StringField('День недели', validators=[DataRequired()])
    start_time = StringField('Начало занятия', validators=[DataRequired()])
    end_time = StringField('Конец занятия', validators=[DataRequired()])
    group = StringField('Учащиеся группы', validators=[DataRequired()])
    teacher = StringField('ФИО преподавателя', validators=[DataRequired()])
    conf_link = StringField('Ссылка на видеоконференцию', validators=[DataRequired()])
    submit = SubmitField('Добавить')
