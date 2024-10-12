from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router

from .forms import Form
from db.db_request.return_status import change_status, return_keyboard
from db.db_request.check_keywords import check_keywords
from db.db_request.return_profile import return_profile
from config import PROMOCODE

router = Router()


@router.message(Form.vip)
async def vip_user(message: Message, state: FSMContext):
    if message.text == PROMOCODE:
        await message.answer('Поздравляем! Вы получили доступ к VIP-аккаунту 100ViPaCcOuNt000')
        change_status(message.chat.id)
        profile = return_profile(message.chat.id)
        check_keywords(message.chat.id, f'{profile[0]} {profile[3]} {profile[4]}')
        await state.set_state(Form.panel)
        await message.answer("Выберите команду", reply_markup=return_keyboard(message.chat.id))
    elif message.text == 'Назад':
        await state.set_state(Form.panel)
        await message.answer("Выберите команду", reply_markup=return_keyboard(message.chat.id))
    else:
        await message.answer('Некорректный запрос')
        await state.set_state(Form.panel)
        await message.answer("Выберите команду", reply_markup=return_keyboard(message.chat.id))
