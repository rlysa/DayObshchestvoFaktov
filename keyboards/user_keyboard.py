from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_instruction = KeyboardButton(text='Инструкция')

user_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
user_keyboard.add(button_instruction)
