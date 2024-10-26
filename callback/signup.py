from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from keyboards.inline import districts_button
from aiogram.fsm.context import FSMContext
from states import FirstCupdownStates

async def get_region_answer(call: CallbackQuery, state: FSMContext):
    region_id = call.data.split(":")[1]
    markup = districts_button(region_id=region_id)
    await state.update_data(region_id=region_id)
    await call.message.answer("Tumaningizni tanlang.", reply_markup=markup)
    await state.set_state(FirstCupdownStates.district)
    await call.message.delete()

async def get_district_answer(call: CallbackQuery, state: FSMContext):
    district_id = call.data.split(":")[1]

    await state.update_data(district_id=district_id)
    await call.message.answer("Siz qaysi maktabda o'qiysiz?", reply_markup=ReplyKeyboardRemove())
    await state.set_state(FirstCupdownStates.school)
    await call.message.delete()

