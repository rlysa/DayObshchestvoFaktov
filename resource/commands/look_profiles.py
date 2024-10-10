from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router
from aiogram.utils.markdown import link

from resource.commands.forms import Form
from db.db_request.profiles_for_looking import profiles_for_looking
from db.db_request.users_likes_unllikes import users_likes_unlikes
from resource.keyboards.likes_keyboard import likes_keyboard, resume_keyboard
from db.db_request.return_status import return_keyboard

router = Router()


@router.message(Form.look_profiles)
async def cmd_look_profiles(message: Message, state: FSMContext):
    if message.text == 'Назад':
        await state.set_state(Form.panel)
        await message.answer('Выберите команду', reply_markup=return_keyboard(message.chat.id))
    else:
        profiles_fl = profiles_for_looking(message.chat.id)
        if message.text == '\U0001F44D':
            ulu = users_likes_unlikes(user_id=message.chat.id, user_id_liked=profiles_fl[0][0], like='users_like')
            if ulu == 1:
                await state.set_state(Form.resume_lp)
                tg_link = f'tg://user?id={profiles_fl[0][0]}'
                await message.answer(f'У вас взаимная симпатия с пользователем <a href="{tg_link}">{profiles_fl[0][1]}</a>',
                                     parse_mode='HTML', reply_markup=resume_keyboard)
            else:
                profiles_fl = profiles_for_looking(message.chat.id)
                if len(profiles_fl) == 0:
                    await state.set_state(Form.panel)
                    await message.answer('Все анкеты просмотрены')
                    await message.answer('Выберите команду', reply_markup=return_keyboard(message.chat.id))
                else:
                    await message.answer(
                        f'{profiles_fl[0][1]}, {profiles_fl[0][2]}, {profiles_fl[0][3]}, {profiles_fl[0][4]}\n\n{profiles_fl[0][5]}',
                        reply_markup=likes_keyboard)
        else:
            users_likes_unlikes(user_id=message.chat.id, user_id_liked=profiles_fl[0][0], like='users_unlike')
            profiles_fl = profiles_for_looking(message.chat.id)
            if len(profiles_fl) == 0:
                await state.set_state(Form.panel)
                await message.answer('Все анкеты просмотрены')
                await message.answer('Выберите команду', reply_markup=return_keyboard(message.chat.id))
            else:
                await message.answer(f'{profiles_fl[0][1]}, {profiles_fl[0][2]}, {profiles_fl[0][3]}, {profiles_fl[0][4]}\n\n{profiles_fl[0][5]}',
                                     reply_markup=likes_keyboard)


@router.message(Form.resume_lp)
async def resume_looking_lp(message: Message, state: FSMContext):
    if message.text == 'Продолжить просмотр анкет':
        profiles_fl = profiles_for_looking(message.chat.id)
        if not profiles_fl:
            await state.set_state(Form.panel)
            await message.answer('Все анкеты просмотрены')
            await message.answer('Выберите команду', reply_markup=return_keyboard(message.chat.id))
        else:
            await state.set_state(Form.look_profiles)
            await message.answer(f'{profiles_fl[0][1]}, {profiles_fl[0][2]}, {profiles_fl[0][3]}, {profiles_fl[0][4]}\n\n{profiles_fl[0][5]}',
                                 reply_markup=likes_keyboard)
    elif message.text == 'Назад':
        await state.set_state(Form.panel)
        await message.answer('Выберите команду', reply_markup=return_keyboard(message.chat.id))
    else:
        await message.answer('Некорректный запрос')

