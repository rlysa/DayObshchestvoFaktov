import asyncio
from aiogram import Bot, Dispatcher

from config import TOKEN, DB_NAME
from db.db_data.db_session import global_init
from resource.commands.start import router as start_router
from resource.commands.profile import router as profile_router
from resource.commands.panel import router as panel_router
from resource.commands.edit_profile import router as my_profile_router

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(profile_router)
dp.include_router(panel_router)
dp.include_router(my_profile_router)


def run_db():
    global_init(DB_NAME)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == '__main__':
    run_db()
    asyncio.run(main())
