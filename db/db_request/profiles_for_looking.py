import sqlite3

from config import DB_NAME


def ids_for_looking(user_id):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    prefer = cursor.execute('SELECT prefer FROM users WHERE user_id="{0}"'.format(user_id)).fetchone()[0]
    profiles_look_early = cursor.execute('SELECT users_like FROM likes WHERE user_id={0}'.format(user_id)).fetchall()[0][0].split() + \
                          cursor.execute('SELECT users_unlike FROM likes WHERE user_id="{0}"'.format(user_id)).fetchall()[0][0].split() +\
                          cursor.execute('SELECT users_mutual FROM likes WHERE user_id="{0}"'.format(user_id)).fetchall()[0][0].split() +\
                          [str(user_id)]
    if prefer == 3:
        profiles_all = [str(i[0]) for i in cursor.execute('SELECT user_id FROM users').fetchall()]
    else:
        profiles_all = [str(i[0]) for i in cursor.execute('SELECT user_id FROM users WHERE sex="{0}"'.format(prefer)).fetchall()]

    profiles_look = list(set(profiles_all) - set(profiles_look_early))
    connection.close()

    return profiles_look


def profiles_for_looking(user_id):
    ids = ids_for_looking(user_id)
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    profiles = []
    for user_id_i in ids:
        profile = list(cursor.execute('SELECT user_id, name, sex, age, city, description FROM users WHERE user_id={0}'.format(user_id_i)).fetchall()[0])
        profile[2] = 'м' if profile[2] == 1 else 'ж'
        rating = list(cursor.execute('SELECT rating FROM likes WHERE user_id={0}'.format(user_id_i)).fetchall()[0])
        profile.append(rating)
        profiles.append(profile)
    profiles.sort(key=lambda x: x[-1], reverse=True)
    connection.close()
    return profiles
