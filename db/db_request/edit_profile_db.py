import sqlite3

from config import DB_NAME
from .check_keywords import check_keywords
from .return_status import return_status
from .return_keywords import return_keywords

from string import punctuation


def edit_field(user_id, field, new_mean):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    old = cursor.execute('SELECT {0} FROM users WHERE user_id={1}'.format(field, user_id)).fetchall()
    new = cursor.execute('UPDATE users SET {0}="{1}" WHERE user_id="{2}"'.format(field, new_mean, user_id))
    if return_status(user_id) == 2:
        kw = return_keywords()[0].split()
        new_mean = new_mean.translate(str.maketrans('', '', punctuation))

        old = ' '.join(list(old[0]))
        old = old.translate(str.maketrans('', '', punctuation))
        count_o = 0
        for i in old.split():
            if i in kw:
                count_o += 1

        count_n = 0
        for i in new_mean.split():
            if i in kw:
                count_n += 1

        rating = cursor.execute('SELECT rating FROM likes WHERE user_id={0}'.format(user_id)).fetchall()[0][0]

        up_rating = cursor.execute('UPDATE likes SET rating={0} WHERE user_id={1}'.format(rating + (count_n - count_o) * 1000, user_id))
    connection.commit()
    connection.close()
