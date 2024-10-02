import sqlalchemy
from .db_session import SqlAlchemyBase


class Likes(SqlAlchemyBase):
    __tablename__ = 'likes'

    id_user = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, unique=True)
    users_like = sqlalchemy.Column(sqlalchemy.String)
    users_unlike = sqlalchemy.Column(sqlalchemy.String)
    users_mutual = sqlalchemy.Column(sqlalchemy.String)
    rating = sqlalchemy.Column(sqlalchemy.Float)
