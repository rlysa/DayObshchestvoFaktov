from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    start = State()
    name = State()
    sex = State()
    age = State()
    city = State()
    description = State()
    photo = State()
    prefer = State()

    panel = State()
    unavailable = State()

    rating = State()
    delete_user = State()

    my_profile = State()
    look_profiles = State()
    who_likes_me = State()
    resume_wlm = State()
    resume_lp = State()

    vip = State()
    keywords = State()

    edit_profile = State()
    new_mean = State()
    new_mean_sex = State()
    end_edit_profile = State()
