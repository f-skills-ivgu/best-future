from flask_wtf import FlaskForm
from wtforms import StringField


class CourierOrder(FlaskForm):
    order_id = StringField('Номер заказа')
    address = StringField('Адрес доставки')
