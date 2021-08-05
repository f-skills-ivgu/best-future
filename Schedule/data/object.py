import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Object(SqlAlchemyBase):
    __tablename__ = 'object'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)


    def __repr__(self):
        return f'{self.id}, {self.name}, '
