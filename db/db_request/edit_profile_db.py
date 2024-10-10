import sqlite3
from config import DB_NAME


def edit_field(user_id, field, new_mean):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    new_name = cursor.execute('UPDATE users SET {0}="{1}" WHERE user_id="{2}"'.format(field, new_mean, user_id))
    connection.commit()
    connection.close()
