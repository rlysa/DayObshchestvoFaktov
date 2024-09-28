from aiogram.filters.command import Command
from aiogram.types import Message

from keyboards.user_keyboard import user_keyboard
from main import bot, dp, Form

import time


@dp.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('Какая-то инструкция', reply_markup=user_keyboard)
    time.sleep(2)
    await Form.name.set()
    await message.answer('Введите Имя')


@dp.message_handler(state=Form.name)
async def process_name(message: Message):
    async with state.proxy() as data:
        data['name'] = message.text

    print(data['name'])
    await Form.age.set()
    await message.reply("How old are you?")
