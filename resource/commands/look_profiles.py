from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router

from resource.commands.forms import Form
from db.db_request.profiles_for_looking import profiles_for_looking, profiles_likes
from resource.keyboards.likes_keyboard import likes_keyboard
from resource.keyboards.user_keyboard import user_keyboard


router = Router()
count = 1


@router.message(Form.look_profiles)
async def look_profiles(message: Message, state: FSMContext):
    global count
    if message.text == 'Назад':
        await state.set_state(Form.panel)
        await message.answer('Выберите команду', reply_markup=user_keyboard)
    else:
        profiles_fl = profiles_for_looking(message.chat.id)
        if message.text == '\U0001F44D':
            profiles_likes(user_id=message.chat.id, user_id_like=profiles_fl[0][0], like='users_like')
        else:
            profiles_likes(user_id=message.chat.id, user_id_like=profiles_fl[0][0], like='users_unlike')
        profiles_fl = profiles_for_looking(message.chat.id)
        if len(profiles_fl) == 0:
            await state.set_state(Form.panel)
            await message.answer('Все анкеты просмотрены')
            await message.answer('Выберите команду', reply_markup=user_keyboard)
        else:
            await message.answer(f'{profiles_fl[0][1]}, {profiles_fl[0][2]}, {profiles_fl[0][3]}, {profiles_fl[0][4]}\n\n{profiles_fl[0][5]}',
                                 reply_markup=likes_keyboard)
