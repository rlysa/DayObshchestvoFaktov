import sqlite3

from config import DB_NAME
from .return_keywords import return_keywords

from string import punctuation


def check_keywords(user_id, text):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    kw = return_keywords()
    text = text.translate(str.maketrans('', '', punctuation))

    count = 0
    for i in text.split():
        if i in kw:
            count += 1
    rating = cursor.execute('SELECT rating FROM likes WHERE user_id={0}'.format(user_id)).fetchall()[0][0]
    up_rating = cursor.execute('UPDATE likes SET rating={0} WHERE user_id={1}'.format(rating + count * 1000, user_id))
    connection.commit()
    connection.close()
