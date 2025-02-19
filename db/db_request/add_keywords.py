import sqlite3

from config import DB_NAME
from db.db_data import db_session
from db.db_data.__all_models import *


def add_keywords():
    db_session.global_init(DB_NAME)
    session = db_session.create_session()
    kw = Keyword(
        password='True',
        list_of_keywords='лиса птица дерево солнце книга умение цветок комната задача луна туча река машина булка друзья музыка снегопад улыбка звезда подарок часы гитара фотография кофе велосипед супергерой команда искусство кот мечта страна поездка арбуз праздник одежда телефон небо картинка пряник зима фрукты уют романтика поэзия искусственный робот мозаика океан историк путешествие техника огонь краска свет искра зубра энергия компьютер апельсин весна ловец тайна лотос диалог пейзаж велосипед квест сказка атлас наука театр глазурь мандала эхо кристалл семя мудрость крепость ураган ритм песня кафе мечта бегемот крылья алмаз шедевр ловкость читатель бумеранг комикс яйца фиалка груша радость танец мелодия тропа открытие кузнечик космос газета отблеск воронка палатка духи формула пустота тень сплав комета опыт уголок берег динозавр хобби'
    )
    session.add(kw)
    session.commit()
    session.close()
