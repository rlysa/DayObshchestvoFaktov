import sqlite3

from config import DB_NAME


def ids_for_looking(user_id):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    prefer = cursor.execute(f'SELECT prefer FROM users WHERE user_id="{user_id}"').fetchone()[0]
    profiles_look_early = cursor.execute(f'SELECT users_like FROM likes WHERE user_id="{user_id}"').fetchall()[0][0].split() + \
                          cursor.execute(f'SELECT users_unlike FROM likes WHERE user_id="{user_id}"').fetchall()[0][0].split() +\
                          cursor.execute(f'SELECT users_mutual FROM likes WHERE user_id="{user_id}"').fetchall()[0][0].split()
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


def profiles_likes(user_id, user_id_like, like):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    users_mutual = cursor.execute(f'SELECT users_like FROM likes WHERE user_id="{user_id_like}"').fetchall()[0][0].split()
    print(users_mutual)
    if str(user_id) in users_mutual and like == 1:
        users1_like = cursor.execute(f'SELECT users_mutual FROM likes WHERE user_id="{user_id}"').fetchall()[0][0]
        users1_like = cursor.execute(f'UPDATE likes SET users_mutual="{users1_like + " " + user_id_like}") WHERE user_id="{user_id}"')
        users2_like = cursor.execute(f'SELECT users_mutual FROM likes WHERE user_id="{user_id_like}"').fetchall()[0][0]
        users1_like = cursor.execute(f'UPDATE likes SET users_mutual="{users2_like + " " + user_id}") WHERE user_id="{user_id_like}"')
    else:
        users_like = cursor.execute(f'SELECT {like} FROM likes WHERE user_id="{user_id}"').fetchall()[0][0]
        users_like = cursor.execute(f'UPDATE likes SET {like}="{users_like + " " + str(user_id_like)}" WHERE user_id="{user_id}"')
    connection.commit()
    connection.close()
