from aiogram.types import Message, CallbackQuery, ContentType
from aiogram.fsm.context import FSMContext
from aiogram import Router

from .forms import Form
from resource.keyboards.sex_keyboard import sex_keyboard, change_sex_keyboard, sex_prefer_keyboard
from db.db_request.add_new_user import add_new_user
from db.db_request.return_status import return_keyboard
from config import ADMIN_PASSWORD

import time

router = Router()

new_user = dict({'user_id': '',
                 'status': '3',
                 'name': '',
                 'sex': 0,
                 'age': 0,
                 'city': '',
                 'description': '',
                 'prefer': 0})


@router.message(Form.name)
async def profile_name(message: Message, state: FSMContext):
    global new_user
    if len(message.text) > 30:
        await message.answer('Вы не можете ввести имя длиной более 30 символов')
        await message.answer('Укажите ваше имя')
    else:
        if message.text == ADMIN_PASSWORD:
            new_user['status'] = 1
            await message.answer('Укажите ваше имя')
        else:
            new_user['user_id'] = message.chat.id
            new_user['name'] = message.text

            time.sleep(1)
            await state.set_state(Form.sex)
            await message.answer('Укажите ваш пол', reply_markup=sex_keyboard)


@router.callback_query(Form.sex)
async def profile_sex(callback: CallbackQuery, state: FSMContext):
    global new_user
    new_user['sex'] = 1 if callback.data == 'м' else 2
    await callback.message.edit_reply_markup(reply_markup=change_sex_keyboard(new_user['sex']))

    time.sleep(1)
    await state.set_state(Form.age)
    await callback.message.answer('Укажите ваш возраст')


@router.message(Form.sex)
async def profile_start(message: Message, state: FSMContext):
    await message.answer('Некорректный запрос')
    await message.answer('Укажите ваш пол', reply_markup=sex_keyboard)


@router.message(Form.age)
async def profile_age(message: Message, state: FSMContext):
    global new_user
    if message.text.isdigit():
        new_user['age'] = int(message.text)
        if int(message.text) >= 14:
            time.sleep(1)
            await state.set_state(Form.city)
            await message.answer('Укажите ваш город')
        else:
            await state.set_state(Form.unavailable)
            await message.answer('Пользователям младше 14 лет бот не доступен к использованию')
    else:
        await message.answer('Возраст указывается числом')
        await message.answer('Укажите ваш возраст')


@router.message(Form.city)
async def profile_city(message: Message, state: FSMContext):
    if len(message.text) > 30:
        await message.answer('Вы не можете ввести название города длиной более 30 символов')
        await message.answer('Укажите ваше город')
    else:
        global new_user
        new_user['city'] = message.text

        time.sleep(1)
        await state.set_state(Form.description)
        await message.answer('Напишите что-то о себе')


@router.message(Form.description)
async def profile_description(message: Message, state: FSMContext):
    if len(message.text) > 200:
        await message.answer('Вы не можете ввести описание длиной более 200 символов')
        await message.answer('Укажите ваше имя')
    else:
        global new_user
        new_user['description'] = message.text

        time.sleep(1)
        await state.set_state(Form.prefer)
        await message.answer('С кем бы вы предпочли знакомиться?', reply_markup=sex_prefer_keyboard)
        # await message.answer('Отправьте фотографию, если не хотите делиться фотографией, напишите "-"')


# @router.message(Form.photo, content_types=ContentType.PHOTO)
# async def profile_photo(message: Message, state: FSMContext):
#     # photo_id = message.photo[-1].file_id
#     # file_path = await message.document
#
#     #photo_data = await bot.download_file(file.file_path)
#
#     # Кодируем фото в Base64
#     #photo_base64 = base64.b64encode(photo_data.getvalue()).decode('utf-8')
#
#     time.sleep(1)
#     await state.set_state(Form.prefer)
#     await message.answer('С кем бы вы предпочли знакомиться?', reply_markup=sex_prefer_keyboard)


@router.callback_query(Form.prefer)
async def profile_sex_prefer(callback: CallbackQuery, state: FSMContext):
    global new_user
    if callback.data == 'м':
        new_user['prefer'] = 1
    elif callback.data == 'ж':
        new_user['prefer'] = 2
    else:
        new_user['prefer'] = 3

    await callback.message.edit_reply_markup(reply_markup=change_sex_keyboard(new_user['prefer']))
    time.sleep(1)
    await state.clear()
    add_new_user(new_user)
    await state.set_state(Form.panel)
    await callback.message.answer('Регистрация пройдена успешно')
    await callback.message.answer("Выберите команду", reply_markup=return_keyboard(callback.message.chat.id))


@router.message(Form.prefer)
async def profile_start(message: Message, state: FSMContext):
    await message.answer('Некорректный запрос')
    await message.answer('С кем бы вы предпочли знакомиться?', reply_markup=sex_prefer_keyboard)


@router.message(Form.unavailable)
async def unavailable(message: Message, state: FSMContext):
    await message.answer('Некорректный запрос')
