from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button = [
        [InlineKeyboardButton(text='Начать заполнение анкеты', callback_data='м')]
    ]

start_keyboard = InlineKeyboardMarkup(inline_keyboard=button)

new_button = [
        [InlineKeyboardButton(text='\U00002705 Начать заполнение анкеты', callback_data='м')]
    ]

change_start_keyboard = InlineKeyboardMarkup(inline_keyboard=new_button)
