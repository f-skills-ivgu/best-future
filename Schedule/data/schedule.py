import sqlalchemy
from .db_session import SqlAlchemyBase


class Schedule(SqlAlchemyBase):
    __tablename__ = 'schedule'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    start_time = sqlalchemy.Column(sqlalchemy.Time, nullable=False)
    end_time = sqlalchemy.Column(sqlalchemy.Time, nullable=False)
    group = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    teacher = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    conf_link = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    def __repr__(self):
        return f'{self.id}, {self.name}, {self.start_time}, {self.end_time}' \
               f'{self.group}, {self.teacher}, {self.conf_link},' \
