import sqlite3

from config import DB_NAME
from db.db_request.return_status import return_status


def users_likes_unlikes(user_id, user_id_liked, like):
    mean_to_return = 0
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    users_liked_likes = cursor.execute('SELECT users_like FROM likes WHERE user_id="{0}"'.format(user_id_liked)).fetchall()[0][0].split()
    if str(user_id) in users_liked_likes and like == 'users_like':
        mean_to_return = 1
        users1_mutual = cursor.execute('SELECT users_mutual FROM likes WHERE user_id="{0}"'.format(user_id)).fetchall()[0][0]
        users1_mutual_up = cursor.execute('UPDATE likes SET users_mutual="{0}" WHERE user_id="{1}"'.format(users1_mutual + str(user_id_liked) + " ", user_id))
        users2_mutual = cursor.execute('SELECT users_mutual FROM likes WHERE user_id="{0}"'.format(user_id_liked)).fetchall()[0][0]
        users1_mutual_up = cursor.execute('UPDATE likes SET users_mutual="{0}" WHERE user_id="{1}"'.format(users2_mutual + str(user_id) + " ", user_id_liked))

    users_like = cursor.execute('SELECT {0} FROM likes WHERE user_id="{1}"'.format(like, user_id)).fetchall()[0][0]
    users_like_up = cursor.execute('UPDATE likes SET {0}="{1}" WHERE user_id="{2}"'.format(like, users_like + str(user_id_liked) + " ", user_id))
    likes_user = cursor.execute('SELECT sbd_likes_user FROM likes WHERE user_id="{0}"'.format(user_id_liked)).fetchall()[0][0]
    unlikes_user = cursor.execute('SELECT sbd_unlikes_user FROM likes WHERE user_id="{0}"'.format(user_id_liked)).fetchall()[0][0]
    if like == 'users_like':
        likes_user_up = cursor.execute('UPDATE likes SET sbd_likes_user="{0}" WHERE user_id="{1}"'.format(likes_user + str(user_id) + " ", user_id_liked))
        rating = cursor.execute('SELECT rating FROM likes WHERE user_id="{0}"'.format(user_id_liked)).fetchall()[0][0]
        if return_status(user_id_liked) != 2:
            rating += 1
        else:
            rating += 100
        users_rating = cursor.execute('UPDATE likes SET rating="{0}" WHERE user_id="{1}"'.format(rating, user_id_liked))
    else:
        unlikes_user_up = cursor.execute('UPDATE likes SET sbd_unlikes_user="{0}" WHERE user_id="{1}"'.format(unlikes_user + str(user_id) + " ", user_id_liked))

    connection.commit()
    connection.close()
    return mean_to_return
