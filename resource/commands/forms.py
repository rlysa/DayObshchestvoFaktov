from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    start = State()
    name = State()
    sex = State()
    age = State()
    city = State()
    description = State()
    prefer = State()

    panel = State()

    my_profile = State()
    instruction = State()
    look_profiles = State()
    who_likes_me = State()

    edit_profile = State()
    new_mean = State()
    new_mean_sex = State()
    end_edit_profile = State()
