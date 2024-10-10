import sqlite3

from config import DB_NAME


def return_statistics():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    count_users = cursor.execute('SELECT user_id FROM users').fetchall()
    print(count_users)
    count_admins = cursor.execute('SELECT user_id FROM users WHERE status=1').fetchall()
    return f'Количество зарегистрированных пользователей: {len(count_users)}\nКоличество админов: {len(count_admins)}'
