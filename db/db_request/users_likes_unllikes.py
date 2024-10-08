import sqlite3

from config import DB_NAME


def users_likes_unlikes(user_id, user_id_liked, like):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    users_liked_likes = cursor.execute(f'SELECT users_like FROM likes WHERE user_id="{user_id_liked}"').fetchall()[0][0].split()
    if str(user_id) in users_liked_likes and like == 'users_like':
        users1_mutual = cursor.execute(f'SELECT users_mutual FROM likes WHERE user_id="{user_id}"').fetchall()[0][0]
        users1_mutual_up = cursor.execute(f'UPDATE likes SET users_mutual="{users1_mutual + str(user_id_liked) + " "}" WHERE user_id="{user_id}"')
        users2_mutual = cursor.execute(f'SELECT users_mutual FROM likes WHERE user_id="{user_id_liked}"').fetchall()[0][0]
        users1_mutual_up = cursor.execute(f'UPDATE likes SET users_mutual="{users2_mutual + str(user_id) + " "}" WHERE user_id="{user_id_liked}"')
    users_like = cursor.execute(f'SELECT {like} FROM likes WHERE user_id="{user_id}"').fetchall()[0][0]
    users_like_up = cursor.execute(f'UPDATE likes SET {like}="{users_like + str(user_id_liked) + " "}" WHERE user_id="{user_id}"')
    likes_user = cursor.execute(f'SELECT sbd_likes_user FROM likes WHERE user_id="{user_id_liked}"').fetchall()[0][0]
    unlikes_user = cursor.execute(f'SELECT sbd_unlikes_user FROM likes WHERE user_id="{user_id_liked}"').fetchall()[0][0]
    if like == 'users_like':
        likes_user_up = cursor.execute(f'UPDATE likes SET sbd_likes_user="{likes_user + str(user_id) + " "}" WHERE user_id="{user_id_liked}"')
    else:
        unlikes_user_up = cursor.execute(f'UPDATE likes SET sbd_unlikes_user="{unlikes_user + str(user_id) + " "}" WHERE user_id="{user_id_liked}"')
    likes_user = cursor.execute(f'SELECT sbd_likes_user FROM likes WHERE user_id="{user_id_liked}"').fetchall()[0][0]
    unlikes_user = cursor.execute(f'SELECT sbd_unlikes_user FROM likes WHERE user_id="{user_id_liked}"').fetchall()[0][0]
    likes = len(likes_user.split())
    unlikes = len(unlikes_user.split())
    users_rating = cursor.execute(f'UPDATE likes SET rating="{round(likes / (likes + unlikes), 2)}" WHERE user_id="{user_id_liked}"')
    connection.commit()
    connection.close()
