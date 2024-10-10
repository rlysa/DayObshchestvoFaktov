import sqlite3

from config import DB_NAME


def return_user(user_id):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    users_id = cursor.execute('SELECT user_id FROM users').fetchall()
    if (user_id,) in users_id:
        return True
    return False


def return_profile(user_id):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    profile = cursor.execute('SELECT name, sex, age, city, description, prefer FROM users WHERE user_id={0}'.format(user_id)).fetchall()
    profile = list(profile[0])
    profile[1] = 'м' if profile[1] == 1 else 'ж'
    if profile[-1] == 1:
        profile[-1] = 'м'
    elif profile[-1] == 2:
        profile[-1] = 'ж'
    else:
        profile[-1] = 'м/ж'
    return profile


if __name__ == '__main__':
    return_profile(1)
