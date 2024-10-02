from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


buttons = [
    [InlineKeyboardButton(text='м', callback_data='м'),
     InlineKeyboardButton(text='ж', callback_data='ж')]
]

sex_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

buttons_prefer = [
    [InlineKeyboardButton(text='м', callback_data='м'),
     InlineKeyboardButton(text='ж', callback_data='ж'),
     InlineKeyboardButton(text='м/ж', callback_data='мж')]
]

sex_prefer_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons_prefer)


def change_sex_keyboard(choose):
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
            [InlineKeyboardButton(text='м/ж', callback_data='мж')]
        ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard
