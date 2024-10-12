from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from .forms import Form
from resource.keyboards.admin_keyboard import admin_rating_keyboard
from db.db_request.return_status import return_keyboard
from db.db_request.full_rating import full_rating, delete_users

from random import choice
from string import ascii_letters, digits, punctuation

router = Router()


@router.message(Form.rating)
async def cmd_full_rating(message: Message, state: FSMContext):
    if message.text == 'Назад':
        await state.set_state(Form.panel)
        await message.answer('Выберите команду', reply_markup=return_keyboard(message.chat.id))
    elif message.text == 'Удалить пользователя':
        await state.set_state(Form.delete_user)
        await message.answer('Введите id пользователя')
    else:
        await message.answer('Некорректный запрос', reply_markup=admin_rating_keyboard)


@router.message(Form.delete_user)
async def cmd_delete_user(message: Message, state: FSMContext):
    if message.text.isdigit():
        if int(message.text) in [i[0] for i in full_rating()]:
            if int(message.text) == message.chat.id:
                await message.answer('Вы не можете удалить себя',
                                     reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Назад')]],
                                                                      resize_keyboard=True))
            else:
                await state.set_state(Form.panel)
                await message.answer('Пользователь удален')
                delete_users(int(message.text))
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
