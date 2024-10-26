from aiogram.fsm.state import State, StatesGroup


class FirstCupdownStates(StatesGroup):
    firstname = State()
    lastname = State()
    job = State()
    phone = State()
    region = State()
    district = State()
    school = State()
    pupil_info = State()
    pupil_class = State()