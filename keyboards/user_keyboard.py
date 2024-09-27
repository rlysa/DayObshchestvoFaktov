from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button_instruction = InlineKeyboardButton('Инструкция', callback_data='button_instruction')

user_keyboard = InlineKeyboardMarkup()
user_keyboard.add(button_instruction)