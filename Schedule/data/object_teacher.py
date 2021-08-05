import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Object_Teacher(SqlAlchemyBase):
    __tablename__ = 'object_teacher'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    object_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("object.id"))
    teacher_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"))

    def __repr__(self):
        return f'{self.id}, {self.object_id}, {self.teacher_id} '
