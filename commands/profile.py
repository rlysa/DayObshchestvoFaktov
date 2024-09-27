from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram import Router

router = Router()


@router.message(Command('Профиль'))
async def cmd_profile(message: Message):
    await message.answer('Настройка профиля')
