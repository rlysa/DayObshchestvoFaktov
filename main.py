import asyncio
from aiogram import Bot, Dispatcher

from config import TOKEN, DB_NAME
from db.db_data.db_session import global_init
from resource.commands.__routers import *
from db.db_request.add_new_user import add_new_user
from db.db_request.delete import delete


bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(profile_router)
dp.include_router(panel_router)
dp.include_router(my_profile_router)
dp.include_router(look_profiles_router)
dp.include_router(who_likes_me_router)
dp.include_router(keywords_router)
dp.include_router(rating_router)
dp.include_router(vip_router)


def run_db():
    global_init(DB_NAME)
    delete()
    add_new_user(dict({'user_id': 100000000,
                       'status': 3,
                       'name': 'Миша',
                       'sex': 1,
                       'age': 18,
                       'city': 'Москва',
                       'description': 'промокод',
                       'prefer': 3}))


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == '__main__':
    run_db()
    asyncio.run(main())

