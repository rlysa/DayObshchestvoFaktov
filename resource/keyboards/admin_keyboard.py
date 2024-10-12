from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttons = [
    [KeyboardButton(text='Моя анкета')],
    [KeyboardButton(text='Смотреть анкеты')],
    [KeyboardButton(text='Кому понравилась моя анкета?')],
    [KeyboardButton(text='Инструкция')],
    [KeyboardButton(text='Статистика'), KeyboardButton(text='Пользователи')]
]

admin_keyboard = ReplyKeyboardMarkup(keyboard=buttons,
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

buttons_rating = [
    [KeyboardButton(text='Назад')],
    [KeyboardButton(text='Удалить пользователя')],
]

admin_rating_keyboard = ReplyKeyboardMarkup(keyboard=buttons_rating,
                                            resize_keyboard=True,
                                            one_time_keyboard=True)
