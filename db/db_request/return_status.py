import sqlite3

from config import DB_NAME
from resource.keyboards.user_keyboard import user_keyboard
from resource.keyboards.admin_keyboard import admin_keyboard


def return_status(user_id):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    status = cursor.execute('SELECT status FROM users WHERE user_id={0}'.format(user_id)).fetchall()[0][0]
    connection.close()
    return status


def return_keyboard(user_id):
    return admin_keyboard if return_status(user_id) == 1 else user_keyboard


def change_status(user_id):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    status = cursor.execute('UPDATE users SET status=2 WHERE user_id={0}'.format(user_id))
    connection.commit()
    connection.close()
