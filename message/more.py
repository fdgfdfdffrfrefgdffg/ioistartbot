from aiogram.types import Message
from sqldata import del_user
from aiogram.enums import ChatType
from aiogram.fsm.context import FSMContext
from keyboards.inline import sub_channels_markup

async def delete_user_answer(message: Message):
    user_id = message.text.split(" ")[1]
    del_user(int(user_id))
    await message.answer("✅ Foydalanuvchi o'chirildi!")

async def sub_channels_answer(message: Message, state: FSMContext):
    context = await state.get_data()
    markup = sub_channels_markup(channels=context.get("channels"))
    if len(context.get("channels")) > 1:
        await message.answer("Quydagi kanallarga obuna bo'ling.", reply_markup=markup)
    else:
        await message.answer("Quydagi kanalga obuna bo'ling.", reply_markup=markup)
    await message.delete()
