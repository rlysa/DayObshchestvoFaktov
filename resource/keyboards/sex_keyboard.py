from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_sex_keyboard():
    buttons = [
        [InlineKeyboardButton(text='м', callback_data='м'),
         InlineKeyboardButton(text='ж', callback_data='ж')]
    ]

    sex_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return sex_keyboard


def change_sex_keyboard(choose):
    if choose == 1:
        button = [
            [InlineKeyboardButton(text='м', callback_data='м')]
        ]
    else:
        button = [
            [InlineKeyboardButton(text='ж', callback_data='ж')]
        ]

    sex_keyboard = InlineKeyboardMarkup(inline_keyboard=button)
    return sex_keyboard


def get_sex_prefer_keyboard():
    buttons_prefer = [
        [InlineKeyboardButton(text='м', callback_data='м'),
         InlineKeyboardButton(text='ж', callback_data='ж'),
         InlineKeyboardButton(text='м/ж', callback_data='мж')]
    ]

    sex_prefer_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons_prefer)
    return sex_prefer_keyboard


def change_sex_prefer_keyboard(choose):
    if choose == 1:
        button = [
            [InlineKeyboardButton(text='м', callback_data='м')]
        ]
    elif choose == 2:
        button = [
            [InlineKeyboardButton(text='ж', callback_data='ж')]
        ]
    else:
        button = [
            [InlineKeyboardButton(text='мж', callback_data='мж')]
        ]

    sex_keyboard = InlineKeyboardMarkup(inline_keyboard=button)
    return sex_keyboard
