import sqlalchemy
from .db_session import SqlAlchemyBase


class Keyword(SqlAlchemyBase):
    __tablename__ = 'keywords'

    password = sqlalchemy.Column(sqlalchemy.String, primary_key=True, unique=True)
    list_of_keywords = sqlalchemy.Column(sqlalchemy.String)
