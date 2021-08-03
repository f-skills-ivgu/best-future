import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Goods(SqlAlchemyBase):
    __tablename__ = 'goods'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    price = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    quantity = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    filling = orm.relation("Filling", back_populates='goods')

    def __repr__(self):
        return f'{self.id}, {self.name}, ' \
               f'{self.price}, {self.quantity}'
