from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router
from aiogram.utils.markdown import link


from .forms import Form
from resource.keyboards.likes_keyboard import likes_keyboard, resume_keyboard
from db.db_request.return_status import return_keyboard
from db.db_request.profiles_like_me import profiles_like_me
from db.db_request.users_likes_unllikes import users_likes_unlikes

router = Router()


@router.message(Form.who_likes_me)
async def cmd_look_who_likes_me(message: Message, state: FSMContext):
    if message.text == 'Назад':
        await state.set_state(Form.panel)
        await message.answer('Выберите команду', reply_markup=return_keyboard(message.chat.id))
    else:
        profiles_lm = profiles_like_me(message.chat.id)
        if message.text == '\U0001F44D':
            ulu = users_likes_unlikes(user_id=message.chat.id, user_id_liked=profiles_lm[0][0], like='users_like')
            if ulu == 1:
                await state.set_state(Form.resume_wlm)
                tg_link = f'tg://user?id={profiles_lm[0][0]}'
                await message.answer(f'У вас взаимная симпатия с пользователем <a href="{tg_link}">{profiles_lm[0][1]}</a>',
                                     parse_mode='HTML', reply_markup=resume_keyboard)
            else:
                if len(profiles_lm) == 0:
                    await state.set_state(Form.panel)
                    await message.answer('Все анкеты просмотрены')
                    await message.answer('Выберите команду', reply_markup=return_keyboard(message.chat.id))
                else:
                    await message.answer(
                        f'{profiles_lm[0][1]}, {profiles_lm[0][2]}, {profiles_lm[0][3]}, {profiles_lm[0][4]}\n\n{profiles_lm[0][5]}',
                        reply_markup=likes_keyboard)
        else:
            users_likes_unlikes(user_id=message.chat.id, user_id_liked=profiles_lm[0][0], like='users_unlike')
            profiles_lm = profiles_like_me(message.chat.id)
            if len(profiles_lm) == 0:
                await state.set_state(Form.panel)
                await message.answer('Все анкеты просмотрены')
                await message.answer('Выберите команду', reply_markup=return_keyboard(message.chat.id))
            else:
                await message.answer(f'{profiles_lm[0][1]}, {profiles_lm[0][2]}, {profiles_lm[0][3]}, {profiles_lm[0][4]}\n\n{profiles_lm[0][5]}',
                                     reply_markup=likes_keyboard)


@router.message(Form.resume_wlm)
async def resume_looking_wlm(message: Message, state: FSMContext):
    if message.text == 'Продолжить просмотр анкет':
        profiles_lm = profiles_like_me(message.chat.id)
        if not profiles_lm:
            await state.set_state(Form.panel)
            await message.answer('Все анкеты просмотрены')
            await message.answer('Выберите команду', reply_markup=return_keyboard(message.chat.id))
        else:
            await state.set_state(Form.who_likes_me)
            await message.answer(f'{profiles_lm[0][1]}, {profiles_lm[0][2]}, {profiles_lm[0][3]}, {profiles_lm[0][4]}\n\n{profiles_lm[0][5]}',
                                 reply_markup=likes_keyboard)
    elif message.text == 'Назад':
        await state.set_state(Form.panel)
        await message.answer('Выберите команду', reply_markup=return_keyboard(message.chat.id))
    else:
        await message.answer('Некорректный запрос')
