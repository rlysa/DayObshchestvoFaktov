from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttons = [
    [KeyboardButton(text='Моя анкета')],
    [KeyboardButton(text='Смотреть анкеты')],
    [KeyboardButton(text='Кому понравилась моя анкета?')],
    [KeyboardButton(text='Инструкция')]
]

user_keyboard = ReplyKeyboardMarkup(keyboard=buttons,
                                    resize_keyboard=True,
                                    one_time_keyboard=True)
