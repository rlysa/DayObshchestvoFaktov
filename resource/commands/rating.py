from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from .forms import Form
from resource.keyboards.admin_keyboard import admin_rating_keyboard
from db.db_request.return_status import return_keyboard
from db.db_request.full_rating import full_rating, change_users_rating

from random import choice
from string import ascii_letters, digits, punctuation

router = Router()


def change_promocode():
    with open('configuration.txt', 'w') as file:
        characters = ascii_letters + digits + punctuation
        password = ''.join(choice(characters) for _ in range(8))
        file.write(password)


@router.message(Form.rating)
async def cmd_full_rating(message: Message, state: FSMContext):
    if message.text == 'Назад':
        await state.set_state(Form.panel)
        await message.answer('Выберите команду', reply_markup=return_keyboard(message.chat.id))
    elif message.text == 'Изменить рейтинг пользователя':
        await state.set_state(Form.change_rating)
        await message.answer('Введите id пользователя, чей рейтинг понизится до 0')
    else:
        await message.answer('Некорректный запрос', reply_markup=admin_rating_keyboard)


@router.message(Form.change_rating)
async def cmd_change_full_rating(message: Message, state: FSMContext):
    if message.text.isdigit():
        if int(message.text) in [i[0] for i in full_rating()]:
            await state.set_state(Form.panel)
            await message.answer('Рейтинг уменьшен')
            change_promocode()
            change_users_rating(int(message.text))
            await message.answer('Выберите команду', reply_markup=return_keyboard(message.chat.id))
        else:
            await message.answer('Некорректный запрос', reply_markup=ReplyKeyboardMarkup(
                keyboard=[[KeyboardButton(text='Назад')]], resize_keyboard=True))
    elif message.text == 'Назад':
        await state.set_state(Form.panel)
        await message.answer('Выберите команду', reply_markup=return_keyboard(message.chat.id))
    else:
        await message.answer('Некорректный запрос', reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text='Назад')]], resize_keyboard=True))
