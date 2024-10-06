import sqlite3

from config import DB_NAME
from db.db_data import db_session
from db.db_data.__all_models import *


def add_new_user(new_user):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    users_id = cursor.execute(f'''SELECT user_id FROM users''').fetchall()
    connection.close()
    db_session.global_init(DB_NAME)
    session = db_session.create_session()
    nu = User(
        user_id=new_user['user_id'],
        name=new_user['name'],
        sex=new_user['sex'],
        age=new_user['age'],
        city=new_user['city'],
        description=new_user['description'],
        prefer=new_user['prefer']
    )
    nl = Likes(
        user_id=new_user['user_id'],
    )
    session.add(nu)
    session.add(nl)
    session.commit()
    session.close()
