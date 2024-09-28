from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router

from .forms import Form

import time

router = Router()


@router.message(Form.name)
async def profile_name(message: Message, state: FSMContext):
    name = message.text

    time.sleep(1)
    await state.set_state(Form.sex)
    await message.answer('Укажите ваш пол')


@router.message(Form.sex)
async def profile_sex(message: Message, state: FSMContext):
    sex = message.text

    time.sleep(1)
    await state.set_state(Form.age)
    await message.answer('Укажите ваш возраст')


@router.message(Form.age)
async def profile_age(message: Message, state: FSMContext):
    age = message.text

    time.sleep(1)
    await state.set_state(Form.city)
    await message.answer('Укажите ваш город')


@router.message(Form.city)
async def profile_city(message: Message, state: FSMContext):
    city = message.text

    time.sleep(1)
    await state.set_state(Form.description)
    await message.answer('Напишите что-то о себе')


@router.message(Form.description)
async def profile_description(message: Message, state: FSMContext):
    description = message.text

    time.sleep(1)
    await state.clear()
    await message.answer('Регистрация пройдена успешно')
