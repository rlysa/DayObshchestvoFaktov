from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    name = State()
    sex = State()
    age = State()
    city = State()
    description = State()
    prefer = State()
