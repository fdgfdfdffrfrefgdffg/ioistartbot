from aiogram.utils.keyboard import InlineKeyboardBuilder
from regions import get_regions, get_districts

regions_markup = InlineKeyboardBuilder()
for region in get_regions():
    regions_markup.button(text=region["name_uz"], callback_data=f"region:{region['id']}")
regions_markup.adjust(1)
regions_markup = regions_markup.as_markup()

def districts_button(region_id):
    markup = InlineKeyboardBuilder()
    districts = get_districts(region_id)
    for districkt in districts:
        markup.button(text=districkt["name_uz"], callback_data=f"district:{districkt['id']}")
    markup.adjust(1)
    return markup.as_markup()

def sub_channels_markup(channels, user_id):
    markup = InlineKeyboardBuilder()
    for channel in channels:
        markup.button(text="Kanalga kirish", url=channel[1])
    markup.button(text="✅ Tekshirish", callback_data=f"checksub:{user_id}")
    markup.adjust(1)
    return markup.as_markup()
