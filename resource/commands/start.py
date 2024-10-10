from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import Router

import time

from .forms import Form
from resource.keyboards.start_keyboard import start_keyboard
from db.db_request.return_status import return_keyboard
from db.db_request.return_profile import return_user

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('''ДайОбществоФактов - бот для знакомств

Длч использования функций данного бота необходимо зарегистрироваться

Доступные функции:
1. Просмотр и изменение личной анкеты
2. Просмотр других анкет, которые можно оценить как "нравится" или "не нравится"
3. Просмотр и оценка анкет людей, которым понравилась ваша анкета

В ленте анкет первыми будут анкеты с более высоким рейтингом, на который влияет количество лайков, которое ставят вашей анкете
Если у вас есть промокод, вы можете повысить анкету до уровня VIP, тогда ваш рейтинг будет расти с большей скоростью''',
                         reply_markup=start_keyboard)
    await state.set_state(Form.start)


@router.callback_query(Form.start)
async def profile_start(callback: CallbackQuery, state: FSMContext):
    time.sleep(0.5)
    await callback.message.edit_reply_markup()
    time.sleep(0.5)
    if return_user(callback.message.chat.id):
        await state.set_state(Form.panel)
        await callback.message.answer('Вы уже зарегистрированы!')
        time.sleep(0.5)
        await callback.message.answer('Выберите команду', reply_markup=return_keyboard(callback.message.chat.id))
    else:
        await callback.message.answer('Заполнение анкеты')
        time.sleep(0.5)
        await callback.message.answer('Укажите ваше имя')
        await state.set_state(Form.name)


@router.message(Form.start)
async def profile_start(message: Message, state: FSMContext):
    await message.answer('Некорректный запрос')
