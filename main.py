import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from config import TOKEN

from commands.profile import router as profile_router
from commands.start import router as start_router

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(profile_router)
dp.include_router(start_router)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
