import sqlalchemy
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    ADMIN = 1
    VIP_USER = 2
    USER = 3

    MALE = 1
    FEMALE = 2
    ANY = 3

    user_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, unique=True)
    status = sqlalchemy.Column(sqlalchemy.Integer)
    name = sqlalchemy.Column(sqlalchemy.String)
    sex = sqlalchemy.Column(sqlalchemy.Integer)
    age = sqlalchemy.Column(sqlalchemy.Integer)
    city = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)
    prefer = sqlalchemy.Column(sqlalchemy.Integer)
    photo = sqlalchemy.Column(sqlalchemy.String, default='')
