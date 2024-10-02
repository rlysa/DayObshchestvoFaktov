import sqlite3

from config import DB_NAME
from db.db_data import db_session
from db.db_data.__all_models import User


def return_user(user_id):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    users_id = cursor.execute(f'SELECT user_id FROM users').fetchall()
    if (user_id,) in users_id:
        return True
    return False


def return_profile(user_id):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    profile = cursor.execute(f'SELECT name, sex, age, city, description FROM users WHERE user_id={user_id}').fetchall()
    profile = list(profile[0])
    profile[1] = 'м' if profile[1] == 1 else 'ж'
    return profile


if __name__ == '__main__':
    return_profile(929513123)
