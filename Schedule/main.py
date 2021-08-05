from flask import Flask, render_template, request
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from werkzeug.exceptions import abort
from werkzeug.utils import redirect
from Schedule.forms.edit_profile import EditProfile
from data.schedule import Schedule
from data.user import User
from data import db_session
from forms.AddLesson import AddLesson
from forms.user import RegisterForm
from forms.LoginForm import loginform
MAX_CONTENT_LENGTH = 1024 * 1024

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init("db/UniversitySchedule.db")

login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    form = loginform()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect('/main_page')
        return render_template('index.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('index.html', title="Главная страница", form=form)


@app.route("/main_page", methods=['GET', 'POST'])
@login_required
def main_page():
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        schedule = db_sess.query(Schedule).all()
    return render_template("schedule.html", schedule=schedule)


@app.route("/lesson", methods=['GET', 'POST'])
@login_required
def add_lesson():
    form = AddLesson()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        schedule = Schedule()
        schedule.name = form.name.data
        schedule.week_day = form.week_day.data
        schedule.start_time = form.start_time.data
        schedule.end_time = form.end_time.data
        schedule.group = form.group.data
        schedule.teacher = form.teacher.data
        schedule.conf_link = form.conf_link.data
        db_sess.add(schedule)
        db_sess.commit()
        return redirect('/lesson')
    return render_template('adding_lesson.html', title='Добавление занятия', form=form)


@app.route('/lesson/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_lesson(id):
    form = AddLesson()
    if request.method == "GET":
        db_sess = db_session.create_session()
        schedule = db_sess.query(Schedule).filter(Schedule.id == id).first()
        if schedule:
            form.name.data = schedule.name
            form.week_day.data = schedule.week_day
            form.start_time.data = schedule.start_time
            form.end_time.data = schedule.end_time
            form.group.data = schedule.group
            form.teacher.data = schedule.teacher
            form.conf_link.data = schedule.conf_link
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        schedule = db_sess.query(Schedule).filter(Schedule.id == id).first()
        if schedule:
            schedule.name = form.name.data
            schedule.week_day = form.week_day.data
            schedule.start_time = form.start_time.data
            schedule.end_time = form.end_time.data
            schedule.group = form.group.data
            schedule.teacher = form.teacher.data
            schedule.conf_link = form.conf_link.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('adding_lesson.html', title='Изменение занятия', form=form)


@app.route('/user_register', methods=['GET', 'POST'])
def user_register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form, message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            role=form.role.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/students', methods=['GET', 'POST'])
@login_required
def print_students():
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        user = db_sess.query(User).filter(User.role == 0).all()
    return render_template("students.html", user=user)


@app.route('/teachers', methods=['GET', 'POST'])
@login_required
def print_teachers():
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        user = db_sess.query(User).filter(User.role == 1).all()
    return render_template("teachers.html", user=user)


@app.route('/profile/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_profile(id):
    form = EditProfile()
    if request.method == "GET":
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.id == id).first()
        if user:
            form.name.data = user.name
            form.note.data = user.note
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.id == id).first()
        if user:
            user.name = form.name.data
            user.note = form.note.data
            db_sess.commit()
            if user.role == 0:
                return redirect('/students')
            if user.role == 1:
                return redirect('/teachers')
        else:
            abort(404)
    return render_template('profile.html', title='Изменение профиля', form=form)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


def main():
    app.run()


if __name__ == '__main__':
    main()