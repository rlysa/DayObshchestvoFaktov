import time

from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from aiogram import Router

from .forms import Form
from resource.keyboards.my_profile_keyboard import edit_profile_keyboard, end_edit_keyboard, my_profile_keyboard
from resource.keyboards.sex_keyboard import sex_keyboard, change_sex_keyboard, sex_prefer_keyboard
from db.db_request.edit_profile_db import edit_field
from db.db_request.return_profile import return_profile
from db.db_request.return_rating import return_rating
from db.db_request.return_status import return_keyboard, return_status
from db.db_request.full_rating import delete_users

router = Router()
field = 0
changes = False


@router.message(Form.my_profile)
async def cmd_my_profile(message: Message, state: FSMContext):
    if message.text == 'Назад':
        await state.set_state(Form.panel)
        await message.answer("Выберите команду", reply_markup=return_keyboard(message.chat.id))
    elif message.text == 'Изменить':
        await state.set_state(Form.edit_profile)
        await message.answer('Что вы хотели бы изменить?', reply_markup=edit_profile_keyboard)
    else:
        await message.answer('Некорректный запрос')
        await message.answer("Выберите команду", reply_markup=my_profile_keyboard)


@router.callback_query(Form.edit_profile)
async def cmd_edit_profile(callback: CallbackQuery, state: FSMContext):
    global field
    if callback.data == 'Имя':
        await callback.message.edit_reply_markup(
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Имя', callback_data='Имя')]]))
        await state.set_state(Form.new_mean)
        field = 'name'
        time.sleep(1)
        await callback.message.answer('Измените имя',
                                      reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Назад')]],
                                                                       resize_keyboard=True))
    elif callback.data == 'Пол':
        await callback.message.edit_reply_markup(
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Пол', callback_data='Пол')]]))
        await state.set_state(Form.new_mean_sex)
        field = 'sex'
        time.sleep(1)
        await callback.message.answer('Измените пол', reply_markup=sex_keyboard)
    elif callback.data == 'Возраст':
        await callback.message.edit_reply_markup(
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[[InlineKeyboardButton(text='Возраст', callback_data='Возраст')]]))
        await state.set_state(Form.new_mean)
        field = 'age'
        time.sleep(1)
        await callback.message.answer('Измените возраст',
                                      reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Назад')]],
                                                                       resize_keyboard=True))
    elif callback.data == 'Город':
        await callback.message.edit_reply_markup(
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[[InlineKeyboardButton(text='Город', callback_data='Город')]]))
        await state.set_state(Form.new_mean)
        field = 'city'
        time.sleep(1)
        await callback.message.answer('Измените город',
                                      reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Назад')]],
                                                                       resize_keyboard=True))
    elif callback.data == 'Описание':
        await callback.message.edit_reply_markup(
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[[InlineKeyboardButton(text='Описание', callback_data='Описание')]]))
        await state.set_state(Form.new_mean)
        field = 'description'
        time.sleep(1)
        await callback.message.answer('Измените информацию о себе',
                                      reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Назад')]],
                                                                       resize_keyboard=True))
    elif callback.data == 'Знакомиться':
        await callback.message.edit_reply_markup(
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[[InlineKeyboardButton(text='С кем знакомиться', callback_data='Знакомиться')]]))
        await state.set_state(Form.new_mean_sex)
        field = 'prefer'
        time.sleep(1)
        await callback.message.answer('Измените предпочтения, с кем бы вы хотели знакомиться',
                                      reply_markup=sex_prefer_keyboard)


@router.message(Form.edit_profile)
async def cmd_edit_profile(message: Message, state: FSMContext):
    global changes
    if message.text == 'Назад':
        if changes:
            await message.answer('Анкета изменена')
            changes = False
            profile = return_profile(message.chat.id)
            await message.answer(f'{profile[0]}, {profile[1]}, {profile[2]}, {profile[3]}\n\n{profile[4]}')
            rating = return_rating(message.chat.id)
            if rating >= 350000:
                await message.answer('Ваш рейтинг уже достиг 350000 3_R5_0at.00_in0.g')
                await message.answer('Afrn\nВаш аккаунт будет удален')
                delete_users(message.chat.id)
            else:
                await message.answer(f'Дополнительная информация:\n\nС кем знакомиться: {profile[-1]}\nРейтинг = {rating}',
                                 reply_markup=return_keyboard(message.chat.id))
        await state.set_state(Form.panel)
        await message.answer('Выберите команду', reply_markup=return_keyboard(message.chat.id))
    else:
        await message.answer('Некорректный запрос')


@router.message(Form.new_mean)
async def cmd_new_mean(message: Message, state: FSMContext):
    global field
    global changes
    if message.text == 'Назад':
        if changes:
            await message.answer('Анкета изменена')
            changes = False
            profile = return_profile(message.chat.id)
            await message.answer(f'{profile[0]}, {profile[1]}, {profile[2]}, {profile[3]}\n\n{profile[4]}')
            rating = return_rating(message.chat.id)
            if rating >= 350000:
                await message.answer('Ваш рейтинг уже достиг 350000 3_R5_0at.00_in0.g')
                await message.answer('Afrn\nВаш аккаунт будет удален')
                delete_users(message.chat.id)
            else:
                await message.answer(f'Дополнительная информация:\n\nС кем знакомиться: {profile[-1]}\nРейтинг = {rating}',
                                 reply_markup=return_keyboard(message.chat.id))
        await state.set_state(Form.panel)
        await message.answer("Выберите команду", reply_markup=return_keyboard(message.chat.id))
    elif field == 'age':
        if not message.text.isdigit():
            await message.answer('Возраст указывается числом')
            await message.answer('Укажите возраст')
        else:
            if int(message.text) >= 14:
                changes = True
                edit_field(message.chat.id, field, int(message.text))
                await state.set_state(Form.end_edit_profile)
                await message.answer('Возраст изменен')
                await message.answer('Хотите внести другие изменения в анкету?', reply_markup=end_edit_keyboard)
            else:
                await state.set_state(Form.unavailable)
                await message.answer('Пользователям младше 14 лет бот не доступен к использованию')
    else:
        if field == 'name':
            if len(message.text) > 30 and return_status(message.chat.id) != 2:
                await message.answer('Вы не можете ввести имя длиной более 30 символов')
                await message.answer('Измените имя')
            elif len(message.text) > 100 and return_status(message.chat.id) == 2:
                await message.answer('Вы не можете ввести имя длиной более 100 символов')
                await message.answer('Измените имя')
            else:
                await message.answer('Имя изменено')
                await message.answer('Хотите внести другие изменения в анкету?', reply_markup=end_edit_keyboard)
                changes = True
                edit_field(message.chat.id, field, message.text)
                await state.set_state(Form.end_edit_profile)
        elif field == 'city':
            if len(message.text) > 30 and return_status(message.chat.id) != 2:
                await message.answer('Вы не можете ввести название города длиной более 30 символов')
                await message.answer('Измените город')
            elif len(message.text) > 100 and return_status(message.chat.id) == 2:
                await message.answer('Вы не можете ввести название города длиной более 100 символов')
                await message.answer('Измените город')
            else:
                await message.answer('Город изменен')
                await message.answer('Хотите внести другие изменения в анкету?', reply_markup=end_edit_keyboard)
                changes = True
                edit_field(message.chat.id, field, message.text)
                await state.set_state(Form.end_edit_profile)
        elif field == 'description':
            if len(message.text) > 200 and return_status(message.chat.id) != 2:
                await message.answer('Вы не можете ввести описание длиной более 200 символов')
                await message.answer('Измените описание')
            elif len(message.text) > 1200 and return_status(message.chat.id) == 2:
                await message.answer('Вы не можете ввести описание длиной более 1200 символов')
                await message.answer('Измените описание')
            else:
                await message.answer('Описание изменено')
                await message.answer('Хотите внести другие изменения в анкету?', reply_markup=end_edit_keyboard)
                changes = True
                edit_field(message.chat.id, field, message.text)
                await state.set_state(Form.end_edit_profile)


@router.callback_query(Form.new_mean_sex)
async def cmd_new_mean_sex(callback: CallbackQuery, state: FSMContext):
    global field
    global changes
    if callback.data == 'м':
        sex = 1
    elif callback.data == 'ж':
        sex = 2
    else:
        sex = 3
    edit_field(callback.message.chat.id, field, sex)
    await callback.message.edit_reply_markup(reply_markup=change_sex_keyboard(sex))
    if field == 'sex':
        await callback.message.answer('Пол изменен')
    else:
        await callback.message.answer('Предпочтения изменены')
    changes = True
    await state.set_state(Form.end_edit_profile)
    await callback.message.answer('Хотите внести другие изменения в анкету?', reply_markup=end_edit_keyboard)


@router.message(Form.new_mean_sex)
async def cmd_new_mean_sex(message: Message, state: FSMContext):
    global changes
    if message.text == 'Назад':
        if changes:
            await message.answer('Анкета изменена')
            profile = return_profile(message.chat.id)
            changes = False
            await message.answer(f'{profile[0]}, {profile[1]}, {profile[2]}, {profile[3]}\n\n{profile[4]}')
            rating = return_rating(message.chat.id)
            if rating >= 350000:
                await message.answer('Ваш рейтинг уже достиг 350000 3_R5_0at.00_in0.g')
                await message.answer('Afrn\nВаш аккаунт будет удален')
                delete_users(message.chat.id)
            else:
                await message.answer(f'Дополнительная информация:\n\nС кем знакомиться: {profile[-1]}\nРейтинг = {rating}',
                                 reply_markup=return_keyboard(message.chat.id))
        await state.set_state(Form.panel)
        await message.answer("Выберите команду", reply_markup=return_keyboard(message.chat.id))
    else:
        await message.answer('Некорректный запрос')


@router.callback_query(Form.end_edit_profile)
async def end_edit_profile(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'Да':
        await callback.message.edit_reply_markup(
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Да', callback_data='Да')]]))
        await state.set_state(Form.edit_profile)
        await callback.message.answer('Что вы хотели бы изменить?', reply_markup=edit_profile_keyboard)
    else:
        await callback.message.edit_reply_markup(
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Нет', callback_data='Нет')]]))
        await callback.message.answer('Анкета изменена')
        profile = return_profile(callback.message.chat.id)
        global changes
        changes = False
        await state.set_state(Form.panel)
        await callback.message.answer(f'{profile[0]}, {profile[1]}, {profile[2]}, {profile[3]}\n\n{profile[4]}')
        rating = return_rating(callback.message.chat.id)
        if rating >= 350000:
            await callback.message.answer('Ваш рейтинг уже достиг 350000 3_R5_0at.00_in0.g')
            await callback.message.answer('Afrn\nВаш аккаунт будет удален')
            delete_users(callback.message.chat.id)
        else:
            await callback.message.answer(f'Дополнительная информация:\n\nС кем знакомиться: {profile[-1]}\nРейтинг = {rating}',
                             reply_markup=return_keyboard(callback.message.chat.id))
            await callback.message.answer("Выберите команду", reply_markup=return_keyboard(callback.message.chat.id))


@router.message(Form.end_edit_profile)
async def end_edit_profile(message: Message, state: FSMContext):
    await message.answer('Некорректный запрос')
