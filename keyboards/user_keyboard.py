from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttons = [
    [KeyboardButton(text='Инструкция')],
    [KeyboardButton(text='Изменить профиль')]
]

user_keyboard = ReplyKeyboardMarkup(keyboard=buttons,
                                    resize_keyboard=True)
                                  # one_time_keyboard=True)

