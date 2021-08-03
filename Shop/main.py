from flask import Flask, render_template
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from werkzeug.utils import redirect
from data.orders import Orders
from data.courier import Courier
from forms.LoginForm import LoginForm
from data.user import User
from forms.user import RegisterForm
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init("db/shop.db")

login_manager = LoginManager()
login_manager.init_app(app)

login_manager2 = LoginManager()
login_manager2.init_app(app)


@app.route("/")
def index():
    return render_template('index.html', title='Главная страница')


@app.route('/user_register', methods=['GET', 'POST'])
def user_register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('user_register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('user_register.html', title='Регистрация',
                                   form=form, message="Такой пользователь уже есть")
        if (form.post.data < 1) & (form.post.data > 3):
            return render_template('user_register.html', title='Регистрация',
                                   form=form, message="Неправильно введен код должности")
        user = User(
            name=form.name.data,
            email=form.email.data,
            post=form.post.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/user_login')
    return render_template('user_register.html', title='Регистрация', form=form)


@app.route('/courier_register', methods=['GET', 'POST'])
def courier_register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('courier_register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(Courier).filter(Courier.email == form.email.data).first():
            return render_template('courier_register.html', title='Регистрация',
                                   form=form, message="Такой пользователь уже есть")
        courier = Courier(
            name=form.name.data,
            email=form.email.data
        )
        courier.set_password(form.password.data)
        db_sess.add(courier)
        db_sess.commit()
        return redirect('/courier_login')
    return render_template('courier_register.html', title='Регистрация', form=form)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@login_manager2.user_loader
def load_user(courier_id):
    db_sess = db_session.create_session()
    return db_sess.query(Courier).get(courier_id)


@app.route('/user_login', methods=['GET', 'POST'])
def user_login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            if user.post == 1:
                return redirect("/user_main/sales-manager")
            if user.post == 2:
                return redirect("/user_main/warehouse-worker")
            if user.post == 3:
                return redirect("/user_main/delivery-manager")
        return render_template('user_login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('user_login.html', title='Авторизация', form=form)


@app.route('/user_main/sales-manager')
def sales_manager_page():
    return 'Страница менеджера по продажам'


@app.route('/user_main/warehouse-worker')
def warehouse_worker_page():
    return 'Страница работника склада'


@app.route('/user_main/delivery-manager')
def delivery_manager_page():
    return 'Страница менеджера по доставке'


@app.route('/courier_login', methods=['GET', 'POST'])
def courier_login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        courier = db_sess.query(Courier).filter(Courier.email == form.email.data).first()
        if courier and courier.check_password(form.password.data):
            login_user(courier, remember=form.remember_me.data)
            return redirect("/courier_main")
        return render_template('courier_login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('courier_login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/courier_main", methods=['GET', 'POST'])
@login_required
def courier_main():
    db_sess = db_session.create_session()
    courier = current_user
    if not courier.status:
        order = db_sess.query(Orders).filter(Orders.courier_id == courier.id).first()
        return render_template('courier_main.html', title='Для курьера', order=order, status='Доставляет')
    else:
        order = db_sess.query(Orders)
        order.address = 'Заказов нет'
        return render_template('courier_main.html', title='Для курьера', status='Свободен', order=order)


@app.route("/user_main")
def user_main():
    return "Приложение для сторудников"


def main():
    app.run()


if __name__ == '__main__':
    main()
