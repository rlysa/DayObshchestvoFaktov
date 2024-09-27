from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery
from aiogram import Router

import time

router = Router()

#async def user_name(callback_query: CallbackQuery):
#    print(callback_query.data)


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('Какая-то инструкция')
    time.sleep(3)
    await message.answer('Введите Имя')
    #await user_name()
