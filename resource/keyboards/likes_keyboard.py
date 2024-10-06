from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

buttons = [
    [KeyboardButton(text='\U0001F44D'), KeyboardButton(text='\U0001F44E')],
    [KeyboardButton(text='Назад')]
]

likes_keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
