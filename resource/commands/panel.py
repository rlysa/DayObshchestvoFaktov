from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import Router

from .forms import Form
from resource.keyboards.user_keyboard import user_keyboard
from resource.keyboards.my_profile_keyboard import my_profile_keyboard
from db.db_request.return_profile import return_profile

router = Router()


@router.message(Form.panel)
async def panel_cmds(message: Message, state: FSMContext):
    if message.text == 'Моя анкета':
        profile = return_profile(message.chat.id)
        await message.answer(f'{profile[0]}, {profile[1]}, {profile[2]}, {profile[3]}\n\n{profile[4]}',
                             reply_markup=my_profile_keyboard)
        await state.set_state(Form.my_profile)
    elif message.text == 'Смотреть анкеты':
        # await state.set_state(Form.look_profiles)
        await message.answer('Функция находится в стадии разработки')
    elif message.text == 'Кому понравилась моя анкета?':
        # await state.set_state(Form.who_likes_me)
        await message.answer('Функция находится в стадии разработки')
    elif message.text == 'Инструкция':
        # await state.set_state(Form.instruction)
        await message.answer('Функция находится в стадии разработки')
