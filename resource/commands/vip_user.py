from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router

from .forms import Form
from db.db_request.return_status import change_status, return_keyboard

router = Router()


def promocode():
    with open('configuration.txt') as file:
        promo = file.readline().strip()
    return promo


@router.message(Form.vip)
async def vip_user(message: Message, state: FSMContext):
    if message.text == promocode():
        await message.answer('Поздравляем! Вы получили доступ к VIP-аккаунту')
        change_status(message.chat.id)
        await state.set_state(Form.panel)
        await message.answer("Выберите команду", reply_markup=return_keyboard(message.chat.id))
    elif message.text == 'Назад':
        await state.set_state(Form.panel)
        await message.answer("Выберите команду", reply_markup=return_keyboard(message.chat.id))
    else:
        await message.answer('Некорректный запрос')
        await message.answer("Выберите команду", reply_markup=return_keyboard(message.chat.id))
