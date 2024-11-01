from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from keyboards.inline import sub_channels_markup
from config import CHANNELS
from aiogram.enums import ChatMemberStatus
from sqldata import get_user
from states import FirstCupdownStates

async def sub_channels_answer(call: CallbackQuery, state: FSMContext, bot: Bot):
    user_id = call.data.split(":")[1]
    if int(user_id) != call.from_user.id:
        await call.answer("❗ Bu tugma siz uchun emas!", show_alert=True)
        return
    not_sub_channels = []
    for channel in CHANNELS:
        member = await bot.get_chat_member(chat_id=channel, user_id=call.from_user.id)
        if member.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR]:
            continue
        not_sub_channels.append((channel, CHANNELS[channel]))
    if not_sub_channels:
        markup = sub_channels_markup(not_sub_channels, call.from_user.id)
        if len(not_sub_channels) > 1:
            await call.message.answer(f"{call.from_user.mention_html('Siz')} quydagi kanallarga obuna bo'lishingiz kerak.", reply_markup=markup, parse_mode="HTML")
        else:
            await call.message.answer(f"{call.from_user.mention_html('Siz')} quydagi kanallarga obuna bo'lishingiz kerak.", reply_markup=markup, parse_mode="HTML")
        await call.answer()
        await call.message.delete()
    else:
        await state.clear()
        if call.message.chat.type == "private":
            if not get_user(user_id=call.from_user.id):

                await call.message.answer("❗ Sizdan hozir ba'zi ma'lumotlarni olaman. Bu ma'lumotlar kurs mentorlarida qoladi. Maqsad sizni olimpiada payti natijangizni ko'rib turish!")
                await call.message.answer("✍️ ISmingizni kiriting. ")
                await state.set_state(FirstCupdownStates.firstname)
            else:
                await call.answer("✅ Mana bu boshqa gap!", show_alert=True)
        else:
            await call.answer("✅ Obuna bo'lganingiz uchun rahmat!", show_alert=True)
        await call.message.delete()