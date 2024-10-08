import sqlite3

from config import DB_NAME


def ids_for_looking(user_id):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    prefer = cursor.execute(f'SELECT prefer FROM users WHERE user_id="{user_id}"').fetchone()[0]
    profiles_look_early = cursor.execute(f'SELECT users_like FROM likes WHERE user_id="{user_id}"').fetchall()[0][0].split() + \
                          cursor.execute(f'SELECT users_unlike FROM likes WHERE user_id="{user_id}"').fetchall()[0][0].split() +\
                          cursor.execute(f'SELECT users_mutual FROM likes WHERE user_id="{user_id}"').fetchall()[0][0].split() +\
                          [str(user_id)]
    if prefer == 3:
        profiles_all = [str(i[0]) for i in cursor.execute(f'SELECT user_id FROM users').fetchall()]
    else:
        profiles_all = [str(i[0]) for i in cursor.execute(f'SELECT user_id FROM users WHERE sex="{prefer}"').fetchall()]

    profiles_look = list(set(profiles_all) - set(profiles_look_early))
    connection.close()

    return profiles_look


def profiles_for_looking(user_id):
    ids = ids_for_looking(user_id)
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    profiles = [list(cursor.execute(f'SELECT user_id, name, sex, age, city, description FROM users WHERE user_id={user_id_i}').fetchall()[0]) for user_id_i in ids]
    for i in profiles:
        i[2] = 'м' if i[2] == 1 else 'ж'
    return profiles
