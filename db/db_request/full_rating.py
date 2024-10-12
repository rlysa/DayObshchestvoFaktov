import sqlite3

from config import DB_NAME


def full_rating():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    rating = [list(i) for i in cursor.execute('SELECT user_id, rating FROM likes').fetchall()]
    rating = sorted(rating, key=lambda x: x[1], reverse=True)
    connection.close()
    return rating


def change_users_rating(user_id):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    change_status = cursor.execute('UPDATE users SET status=3 WHERE user_id={0}'.format(user_id))
    change_rating = cursor.execute('UPDATE likes SET rating=0 WHERE user_id={0}'.format(user_id))
    connection.commit()
    connection.close()
