import sqlite3

from config import DB_NAME


def return_keywords():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    kw = list(cursor.execute('SELECT list_of_keywords FROM keywords WHERE password="True"').fetchall()[0])
    connection.close()
    return kw
