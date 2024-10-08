from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router

from .forms import Form
from resource.keyboards.likes_keyboard import likes_keyboard
from resource.keyboards.user_keyboard import user_keyboard
from db.db_request.profiles_like_me import profiles_like_me
from db.db_request.users_likes_unllikes import users_likes_unlikes

router = Router()


@router.message(Form.who_likes_me)
async def look_profiles_like_me(message: Message, state: FSMContext):
    if message.text == 'Назад':
        await state.set_state(Form.panel)
        await message.answer('Выберите команду', reply_markup=user_keyboard)
    else:
        profiles_lm = profiles_like_me(message.chat.id)
        if message.text == '\U0001F44D':
            users_likes_unlikes(user_id=message.chat.id, user_id_liked=profiles_lm[0][0], like='users_like')
        else:
            users_likes_unlikes(user_id=message.chat.id, user_id_liked=profiles_lm[0][0], like='users_unlike')
        profiles_lm = profiles_like_me(message.chat.id)
        if len(profiles_lm) == 0:
            await state.set_state(Form.panel)
            await message.answer('Все анкеты просмотрены')
            await message.answer('Выберите команду', reply_markup=user_keyboard)
        else:
            await message.answer(f'{profiles_lm[0][1]}, {profiles_lm[0][2]}, {profiles_lm[0][3]}, {profiles_lm[0][4]}\n\n{profiles_lm[0][5]}',
                                 reply_markup=likes_keyboard)
