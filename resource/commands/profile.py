from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import Router

from .forms import Form
from resource.keyboards.user_keyboard import user_keyboard
from resource.keyboards.sex_keyboard import get_sex_keyboard, change_sex_keyboard, get_sex_prefer_keyboard, change_sex_prefer_keyboard
from db.db_request.add_new_user import add_new_user

import time

router = Router()

new_user = dict({'user_id': '',
                 'name': '',
                 'sex': '',
                 'age': 0,
                 'city': '',
                 'description': '',
                 'prefer': ''})


@router.message(Form.name)
async def profile_name(message: Message, state: FSMContext):
    global new_user
    new_user['user_id'] = message.chat.id
    new_user['name'] = message.text

    time.sleep(1)
    await state.set_state(Form.sex)
    await message.answer('Укажите ваш пол', reply_markup=get_sex_keyboard())


@router.callback_query(Form.sex)
async def profile_sex(callback: CallbackQuery, state: FSMContext):
    global new_user
    new_user['sex'] = 1 if callback.data == 'м' else 2
    await callback.message.edit_reply_markup(reply_markup=change_sex_keyboard(new_user['sex']))

    time.sleep(1)
    await state.set_state(Form.age)
    await callback.message.answer('Укажите ваш возраст')


@router.message(Form.age)
async def profile_age(message: Message, state: FSMContext):
    global new_user
    if message.text.isdigit():
        new_user['age'] = message.text

        time.sleep(1)
        await state.set_state(Form.city)
        await message.answer('Укажите ваш город')
    else:
        await message.answer('Возраст указывается числом')
        await message.answer('Укажите ваш возраст')


@router.message(Form.city)
async def profile_city(message: Message, state: FSMContext):
    global new_user
    new_user['city'] = message.text

    time.sleep(1)
    await state.set_state(Form.description)
    await message.answer('Напишите что-то о себе')


@router.message(Form.description)
async def profile_description(message: Message, state: FSMContext):
    global new_user
    new_user['description'] = message.text

    time.sleep(1)
    await state.set_state(Form.prefer)
    await message.answer('С кем бы вы предпочли знакомиться?', reply_markup=get_sex_prefer_keyboard())


@router.callback_query(Form.prefer)
async def profile_sex_prefer(callback: CallbackQuery, state: FSMContext):
    global new_user
    if callback.data == 'м':
        new_user['prefer'] = 1
    elif callback.data == 'ж':
        new_user['prefer'] = 2
    else:
        new_user['prefer'] = 3

    await callback.message.edit_reply_markup(reply_markup=change_sex_prefer_keyboard(new_user['prefer']))
    time.sleep(1)
    await state.clear()
    add_new_user(new_user)
    await callback.message.answer('Регистрация пройдена успешно', reply_markup=user_keyboard)
