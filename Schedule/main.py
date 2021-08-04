from flask import Flask, render_template
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from werkzeug.utils import redirect
from data.schedule import Schedule
from data.user import User
from data import db_session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init("db/UniversitySchedule.db")

login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/")
def index():
    return render_template('index.html', title='Главная страница')


def main():
    app.run()


if __name__ == '__main__':
    main()
