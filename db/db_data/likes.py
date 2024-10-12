import sqlalchemy
from .db_session import SqlAlchemyBase


class Likes(SqlAlchemyBase):
    __tablename__ = 'likes'

    user_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, unique=True)
    users_like = sqlalchemy.Column(sqlalchemy.String, default='')
    users_unlike = sqlalchemy.Column(sqlalchemy.String, default='')
    users_mutual = sqlalchemy.Column(sqlalchemy.String, default='')
    sbd_likes_user = sqlalchemy.Column(sqlalchemy.String, default='')
    sbd_unlikes_user = sqlalchemy.Column(sqlalchemy.String, default='')
    rating = sqlalchemy.Column(sqlalchemy.Integer, default=0)
