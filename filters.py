from aiogram import Bot
from aiogram.types import Message
from aiogram.filters import Filter
from aiogram.fsm.context import FSMContext
from aiogram.enums import ChatMemberStatus
from sqldata import get_user
from config import CHANNELS

class CheckUser(Filter):
    async def __call__(self, message: Message):
        return not get_user(user_id=message.from_user.id) and message.chat.type == "private"

class CheckSubChannels(Filter):
    async def __call__(self, message: Message, state: FSMContext, bot: Bot):
        not_sub_channels = []
        for channel in CHANNELS:
            member = await bot.get_chat_member(chat_id=channel, user_id=message.from_user.id)
            if member.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR]:
                continue
            not_sub_channels.append((channel, CHANNELS[channel]))
        if not_sub_channels:
            await state.update_data(channels=not_sub_channels)
            return True
        return False