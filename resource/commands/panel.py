from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import Router
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from .forms import Form
from resource.keyboards.my_profile_keyboard import my_profile_keyboard
from resource.keyboards.likes_keyboard import likes_keyboard
from db.db_request.return_profile import return_profile
from db.db_request.profiles_for_looking import profiles_for_looking
from db.db_request.profiles_like_me import profiles_like_me
from db.db_request.return_status import return_keyboard, return_status, change_status
from db.db_request.return_statistics import return_statistics
from db.db_request.return_rating import return_rating
from db.db_request.full_rating import full_rating
from resource.keyboards.admin_keyboard import admin_rating_keyboard
from db.db_request.check_keywords import check_keywords

router = Router()


@router.message(Form.panel)
async def cmds_panel(message: Message, state: FSMContext):
    if message.text == 'Моя анкета':
        profile = return_profile(message.chat.id)
        # await message.answer_photo(photo='', caption=f'{profile[0]}, {profile[1]}, {profile[2]}, {profile[3]}\n\n{profile[4]}')
        await message.answer(f'{profile[0]}, {profile[1]}, {profile[2]}, {profile[3]}\n\n{profile[4]}')
        await message.answer(f'Дополнительная информация:\n\nС кем знакомиться: {profile[-1]}\nРейтинг = {return_rating(message.chat.id)}',
                             reply_markup=my_profile_keyboard)
        await state.set_state(Form.my_profile)
    elif message.text == 'Смотреть анкеты':
        profiles_fl = profiles_for_looking(message.chat.id)
        if not profiles_fl:
            await message.answer('Все анкеты просмотрены')
            await message.answer('Выберите команду', reply_markup=return_keyboard(message.chat.id))
        else:
            await state.set_state(Form.look_profiles)
            await message.answer(f'{profiles_fl[0][1]}, {profiles_fl[0][2]}, {profiles_fl[0][3]}, {profiles_fl[0][4]}\n\n{profiles_fl[0][5]}',
                                 reply_markup=likes_keyboard)
    elif message.text == 'Кому понравилась моя анкета?':
        profiles_lm = profiles_like_me(message.chat.id)
        if not profiles_lm:
            await message.answer('Все анкеты просмотрены')
            await message.answer('Выберите команду', reply_markup=return_keyboard(message.chat.id))
        else:
            await state.set_state(Form.who_likes_me)
            await message.answer(
                f'{profiles_lm[0][1]}, {profiles_lm[0][2]}, {profiles_lm[0][3]}, {profiles_lm[0][4]}\n\n{profiles_lm[0][5]}',
                reply_markup=likes_keyboard)
    elif message.text == 'Инструкция':
        await message.answer('''ДайОбществоФактов - бот для знакомств

Длч использования функций данного бота необходимо зарегистрироваться

Доступные функции:
1. Просмотр и изменение личной анкеты
2. Просмотр других анкет, которые можно оценить как "нравится" или "не нравится"
3. Просмотр и оценка анкет людей, которым понравилась ваша анкета

В ленте анкет первыми будут анкеты с более высоким рейтингом, на который влияет количество лайков, которое ставят вашей анкете
Если у вас есть промокод, вы можете повысить анкету до уровня VIP, тогда ваш рейтинг будет расти с большей скоростью''')
        await message.answer("Выберите команду", reply_markup=return_keyboard(message.chat.id))
    elif message.text == 'Статистика' and return_status(message.chat.id) == 1:
        await message.answer(return_statistics())
        await message.answer("Выберите команду", reply_markup=return_keyboard(message.chat.id))
    elif message.text == 'Пользователи' and return_status(message.chat.id) == 1:
        rating = ''
        fr = full_rating()
        for i in range(len(fr)):
            rating += f'\n{i + 1}. {fr[i][1]} - {fr[i][0]}'
        await state.set_state(Form.rating)
        await message.answer(rating, reply_markup=admin_rating_keyboard)
    elif message.text == 'VIP':
        if return_rating(message.chat.id) > 100000 and return_status(message.chat.id) == 3:
            await message.answer('Поздравляем! Вы получили доступ к VIP-аккаунту 100ViPaCcOuNt000')
            change_status(message.chat.id)
            profile = return_profile(message.chat.id)
            check_keywords(message.chat.id, f'{profile[0]} {profile[3]} {profile[4]}')
            await message.answer("Выберите команду", reply_markup=return_keyboard(message.chat.id))
        elif return_status(message.chat.id) == 3:
            await state.set_state(Form.vip)
            await message.answer('Введите промокод или достигнете рейтинга больше 100000',
                                 reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Назад')]],
                                                                  resize_keyboard=True))
        elif return_status(message.chat.id) == 1:
            await message.answer('Вы не можете перейти на роль ниже')
            await message.answer("Выберите команду", reply_markup=return_keyboard(message.chat.id))
        else:
            await message.answer('У вас уже есть VIP-аккаунт')
            await message.answer("Выберите команду", reply_markup=return_keyboard(message.chat.id))
    elif message.text == 'Рейтинг' and return_status(message.chat.id) == 2:
        await state.set_state(Form.keywords)
        await message.answer('Некорректный запрос')
        await message.answer("Выберите команду", reply_markup=return_keyboard(message.chat.id))
    else:
        await message.answer('Некорректный запрос')
        await message.answer("Выберите команду", reply_markup=return_keyboard(message.chat.id))
