import sqlite3

from config import DB_NAME


def return_rating(user_id):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    rating = cursor.execute('SELECT rating FROM likes WHERE user_id={0}'.format(user_id)).fetchall()[0][0]
    connection.close()
    return rating
