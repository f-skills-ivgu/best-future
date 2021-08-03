import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Filling(SqlAlchemyBase):
    __tablename__ = 'filling'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    order_id = sqlalchemy.Column(sqlalchemy.Integer,
                                 sqlalchemy.ForeignKey("order.id"))
    order = orm.relation('Orders')

    goods_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("goods.id"))
    goods = orm.relation('Goods')

    quantity = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    def __repr__(self):
        return f'{self.id}, {self.order_id}, ' \
               f'{self.goods_id}, {self.quantity}'
