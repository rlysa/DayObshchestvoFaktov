import sqlite3

from config import DB_NAME


def users_likes_unlikes(user_id, user_id_liked, like):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    users_liked_likes = cursor.execute(f'SELECT users_like FROM likes WHERE user_id="{user_id_liked}"').fetchall()[0][0].split()
    print(users_liked_likes)
    print(user_id, type(user_id))
    if str(user_id) in users_liked_likes and like == 'users_like':
        users1_like = cursor.execute(f'SELECT users_mutual FROM likes WHERE user_id="{user_id}"').fetchall()[0][0]
        users1_like = cursor.execute(f'UPDATE likes SET users_mutual="{users1_like + str(user_id_liked) + " "}" WHERE user_id="{user_id}"')
        users2_like = cursor.execute(f'SELECT users_mutual FROM likes WHERE user_id="{user_id_liked}"').fetchall()[0][0]
        users1_like = cursor.execute(f'UPDATE likes SET users_mutual="{users2_like + str(user_id) + " "}" WHERE user_id="{user_id_liked}"')
    else:
        users_like = cursor.execute(f'SELECT {like} FROM likes WHERE user_id="{user_id}"').fetchall()[0][0]
        users_like = cursor.execute(f'UPDATE likes SET {like}="{users_like + str(user_id_liked) + " "}" WHERE user_id="{user_id}"')
        if like == 'users_like':
            likes_user = cursor.execute(f'SELECT sbd_likes_user FROM likes WHERE user_id="{user_id_liked}"').fetchall()[0][0]
            likes_user = cursor.execute(f'UPDATE likes SET sbd_likes_user="{likes_user + str(user_id) + " "}" WHERE user_id="{user_id_liked}"')
        else:
            unlikes_user = cursor.execute(f'SELECT sbd_unlikes_user FROM likes WHERE user_id="{user_id_liked}"').fetchall()[0][0]
            unlikes_user = cursor.execute(f'UPDATE likes SET sbd_unlikes_user="{unlikes_user + str(user_id) + " "}" WHERE user_id="{user_id_liked}"')
    connection.commit()
    connection.close()
