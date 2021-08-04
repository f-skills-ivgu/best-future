from flask import Flask, render_template
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from werkzeug.utils import redirect

from forms.user import RegisterForm
from data.schedule import Schedule
from data.user import User
from data import db_session
from forms.LoginForm import loginform

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
        return render_template('user_login.html',
                               message="Неправильный логин или пароль",
                               form=form)
        if user.role == 1:
            return redirect('/admin')
    return render_template('index.html', title="Главная страница", form=form)


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




def main():
    app.run()


if __name__ == '__main__':
    main()