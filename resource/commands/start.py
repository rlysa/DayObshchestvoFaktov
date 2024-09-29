from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import Router

import time

from .forms import Form
from resource.keyboards.start_keyboard import start_keyboard

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('''ДайОбществоФактов - бот для знакомств
    
Как он работает?
1. Вы заполняете анкету о себе, которую в любой момент можно изменить
2. После заполнения анкеты вам доступна функция просмотра других анкет, которые вы мо жете оценить как "нравится" или "не нравится"
3. Также вам доступна функция просмотра анкет людей, которым понравились вы, эти анкеты тоже можно оценить
4. Если с понравившимся вам человеком взаимная симпатия, есть возможность перейти в личные сообщения для дальнейшего знакомства''',
                         reply_markup=start_keyboard)
    await state.set_state(Form.start)


@router.callback_query(Form.start)
async def profile_start(callback: CallbackQuery, state: FSMContext):
    time.sleep(0.5)
    await callback.message.edit_reply_markup()
    time.sleep(0.5)
    await callback.message.answer('Заполнение анкеты')
    time.sleep(0.5)
    await callback.message.answer('Укажите ваше имя')
    await state.set_state(Form.name)
