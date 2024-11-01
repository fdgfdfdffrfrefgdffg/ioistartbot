from aiogram.types import Message
from sqldata import del_user
from aiogram.enums import ChatType
from aiogram.fsm.context import FSMContext
from keyboards.inline import sub_channels_markup
from aiogram.types import FSInputFile
import os
from config import ADMINS



async def forward_msg(message: Message):
    if not message.from_user.id in ADMINS:
        for admin in ADMINS:
            await message.forward(chat_id=admin) 
            await message.answer("✅ Xabar adminga yetkazildi!")
    

async def send_db_file(message: Message):
    if message.from_user.id != 5165396993:
        return
    await message.answer_document(FSInputFile("data.db"), caption="Mana, data.db fayli.")
    
async def delete_user_answer(message: Message):
    user_id = message.text.split(" ")[1]
    del_user(int(user_id))
    await message.answer("✅ Foydalanuvchi o'chirildi!")

async def sub_channels_answer(message: Message, state: FSMContext):
    context = await state.get_data()
    markup = sub_channels_markup(channels=context.get("channels"), user_id=message.from_user.id)
    if len(context.get("channels")) > 1:
        await message.answer(f"{message.from_user.mention_html('Siz')} quydagi kanallarga obuna bo'lishingiz kerak.", reply_markup=markup, parse_mode="HTML")
    else:
        await message.answer(f"{message.from_user.mention_html('Siz')} quydagi kanallarga obuna bo'lishingiz kerak.", reply_markup=markup, parse_mode="HTML")
    await message.delete()

async def get_chat_id(message: Message):
    await message.answer(f"Chat ID: {message.chat.id}")
