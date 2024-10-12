import sqlite3

from config import DB_NAME


def delete():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    delete_u = cursor.execute('DELETE FROM users')
    delete_u = cursor.execute('DELETE FROM likes')
    delete_u = cursor.execute('DELETE FROM keywords')
    connection.commit()
    connection.close()
