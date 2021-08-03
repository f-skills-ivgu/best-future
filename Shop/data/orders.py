import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Orders(SqlAlchemyBase):
    __tablename__ = 'order'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    status = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    manager_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey("user.id"))
    manager = orm.relation("User")

    courier_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey("courier.id"))
    courier = orm.relation("Courier")

    filling = orm.relation("Filling", back_populates='order')

    def __repr__(self):
        return f'{self.id}, {self.address}, ' \
               f'{self.status}, {self.manager_id}, {self.courier_id}, {self.filling}'
