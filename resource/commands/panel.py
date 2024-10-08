from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import Router

from .forms import Form
from resource.keyboards.user_keyboard import user_keyboard
from resource.keyboards.my_profile_keyboard import my_profile_keyboard
from resource.keyboards.likes_keyboard import likes_keyboard
from db.db_request.return_profile import return_profile
from db.db_request.profiles_for_looking import profiles_for_looking
from db.db_request.profiles_like_me import profiles_like_me


router = Router()


@router.message(Form.panel)
async def panel_cmds(message: Message, state: FSMContext):
    if message.text == 'Моя анкета':
        profile = return_profile(message.chat.id)
        await message.answer(f'{profile[0]}, {profile[1]}, {profile[2]}, {profile[3]}\n\n{profile[4]}')
        await message.answer(f'С кем знакомиться: {profile[-1]}', reply_markup=my_profile_keyboard)
        await state.set_state(Form.my_profile)
    elif message.text == 'Смотреть анкеты':
        profiles_fl = profiles_for_looking(message.chat.id)
        if not profiles_fl:
            await message.answer('Все анкеты просмотрены')
            await message.answer('Выберите команду', reply_markup=user_keyboard)
        else:
            await state.set_state(Form.look_profiles)
            await message.answer(f'{profiles_fl[0][1]}, {profiles_fl[0][2]}, {profiles_fl[0][3]}, {profiles_fl[0][4]}\n\n{profiles_fl[0][5]}',
                                 reply_markup=likes_keyboard)
    elif message.text == 'Кому понравилась моя анкета?':
        profiles_lm = profiles_like_me(message.chat.id)
        if not profiles_lm:
            await message.answer('Все анкеты просмотрены')
            await message.answer('Выберите команду', reply_markup=user_keyboard)
        else:
            await state.set_state(Form.who_likes_me)
            await message.answer(
                f'{profiles_lm[0][1]}, {profiles_lm[0][2]}, {profiles_lm[0][3]}, {profiles_lm[0][4]}\n\n{profiles_lm[0][5]}',
                reply_markup=likes_keyboard)
    elif message.text == 'Инструкция':
        await message.answer('''ДайОбществоФактов - бот для знакомств

Как он работает?
1. Вы заполняете анкету о себе, которую в любой момент можно изменить
2. После заполнения анкеты вам доступна функция просмотра других анкет, которые вы мо жете оценить как "нравится" или "не нравится"
3. Также вам доступна функция просмотра анкет людей, которым понравились вы, эти анкеты тоже можно оценить
4. Если с понравившимся вам человеком взаимная симпатия, есть возможность перейти в личные сообщения для дальнейшего знакомства''')
        await message.answer("Выберите команду", reply_markup=user_keyboard)
    else:
        await message.answer('Некорректный запрос')
        await message.answer("Выберите команду", reply_markup=user_keyboard)
