from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

buttons = [
    [KeyboardButton(text='Изменить')],
    [KeyboardButton(text='Назад')]
]

my_profile_keyboard = ReplyKeyboardMarkup(keyboard=buttons,
                                          resize_keyboard=True)

edit_buttons = [
    [InlineKeyboardButton(text='Имя', callback_data='Имя'),
     InlineKeyboardButton(text='Пол', callback_data='Пол')],
    [InlineKeyboardButton(text='Возраст', callback_data='Возраст'),
     InlineKeyboardButton(text='Город', callback_data='Город')],
    [InlineKeyboardButton(text='Описание', callback_data='Описание')],
    [InlineKeyboardButton(text='С кем знакомиться', callback_data='Знакомиться')]
]

edit_profile_keyboard = InlineKeyboardMarkup(inline_keyboard=edit_buttons)

end_edit_buttons = [
    [InlineKeyboardButton(text='Да', callback_data='Да'),
     InlineKeyboardButton(text='Нет', callback_data='Нет')],
]

end_edit_keyboard = InlineKeyboardMarkup(inline_keyboard=end_edit_buttons)
