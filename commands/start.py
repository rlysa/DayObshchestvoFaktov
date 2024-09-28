from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router

import time

# from keyboards.user_keyboard import user_keyboard

from .forms import Form

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('Какая-то инструкция')
    time.sleep(2)
    await state.set_state(Form.name)
    await message.answer('Укажите ваше имя')
