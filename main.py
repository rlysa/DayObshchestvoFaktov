import asyncio
from aiogram import Bot, Dispatcher, types
from config import TOKEN
from commands.start import router as start_router
from commands.profile import router as profile_router

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(profile_router)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
