import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.state import StatesGroup, State

from config import TOKEN

from commands.profile import router as profile_router

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(profile_router)


class Form(StatesGroup):
    name = State()
    sex = State()
    age = State()
    city = State()
    description = State()


from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

import time


@dp.message(Command('start'))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('Какая-то инструкция')
    time.sleep(2)
    await state.set_state(Form.name)
    await message.answer('Укажите ваше имя')


@dp.message(Form.name)
async def profile_name(message: Message, state: FSMContext):
    name = message.text

    await state.set_state(Form.sex)
    await message.answer('Укажите ваш пол')


@dp.message(Form.sex)
async def profile_name(message: Message, state: FSMContext):
    sex = message.text

    await state.set_state(Form.age)
    await message.answer('Укажите ваш возраст')


@dp.message(Form.age)
async def profile_age(message: Message, state: FSMContext):
    age = message.text

    await state.set_state(Form.city)
    await message.answer('Укажите ваш город')


@dp.message(Form.city)
async def profile_age(message: Message, state: FSMContext):
    city = message.text

    await state.set_state(Form.description)
    await message.answer('Напишите что-то о себе')


@dp.message(Form.description)
async def profile_age(message: Message, state: FSMContext):
    description = message.text

    await state.clear()
    await message.answer('Регистрация пройдена успешно')


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
