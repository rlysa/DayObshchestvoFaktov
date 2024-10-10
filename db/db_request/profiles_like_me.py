import sqlite3

from config import DB_NAME


def profiles_like_me(user_id):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    ids_lm = cursor.execute('SELECT sbd_likes_user FROM likes WHERE user_id="{0}"'.format(user_id)).fetchall()[0][0].split()
    profiles_look_early = cursor.execute('SELECT users_like FROM likes WHERE user_id="{0}"'.format(user_id)).fetchall()[0][0].split() + \
                          cursor.execute('SELECT users_unlike FROM likes WHERE user_id="{0}"'.format(user_id)).fetchall()[0][0].split() + \
                          cursor.execute('SELECT users_mutual FROM likes WHERE user_id="{0}"'.format(user_id)).fetchall()[0][0].split()

    profiles_lm = []
    for user_id_i in ids_lm:
        profile = list(cursor.execute('SELECT user_id, name, sex, age, city, description FROM users WHERE user_id={0}'.format(user_id_i)).fetchall()[0])
        profile[2] = 'м' if profile[2] == 1 else 'ж'
        rating = list(cursor.execute('SELECT rating FROM likes WHERE user_id={0}'.format(user_id_i)).fetchall()[0])
        profile.append(rating)
        profiles_lm.append(profile)
    profiles_lm = sorted(profiles_lm, key=lambda x: x[-1], reverse=True)
    connection.close()
    return profiles_lm
