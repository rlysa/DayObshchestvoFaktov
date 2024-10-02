import sqlite3
from config import DB_NAME


def edit_field(user_id, field, new_mean):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    new_name = cursor.execute(f'UPDATE users SET {field}="{new_mean}" WHERE user_id={user_id}')
    connection.commit()
    connection.close()
