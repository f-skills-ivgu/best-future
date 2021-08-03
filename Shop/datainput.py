from flask import Flask

from data import db_session
from data.orders import Orders

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    order = Orders()
    order.address = "гончарова 12"
    order.status = 4
    order.manager_id = 1
    order.courier_id = 1
    db_sess = db_session.create_session()
    db_sess.add(order)
    db_sess.commit()


if __name__ == '__main__':
    main()
