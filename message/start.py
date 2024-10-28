from aiogram import Bot
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from states import FirstCupdownStates
from keyboards.reply import phone_markup, select_job_markup, class_button
from keyboards.inline import regions_markup
from regions import get_region, get_district
from sqldata import add_user, add_teacher, add_pupil

async def start_answer(message: Message):
    await message.answer("Assalomu alaykum, kursga ro'yhatga olish tugadi!")

async def start_command_answer(message: Message):
    await message.answer("❗ Siz ro'yhatdan o'tgansiz! Hozirda bot faqat ro'yhatdan o'tkazish uchun xizmat qilmoqda")

async def first_cupdown_answer(message: Message, state: FSMContext):
    await message.answer("❗ Sizdan hozir ba'zi ma'lumotlarni olaman. Bu ma'lumotlar kurs mentorlarida qoladi. Maqsad sizni olimpiada payti natijangizni ko'rib turish!")
    await message.answer("✍️ ISmingizni kiriting. ")
    await state.set_state(FirstCupdownStates.firstname)

async def get_firstname_answer(message: Message, state: FSMContext):
    await message.reply("Yaxshi")
    await state.update_data(firstname=message.text)
    await message.answer("✍️ Familyangizni kiriting.")
    await state.set_state(FirstCupdownStates.lastname)

async def get_lastname_answer(message: Message, state: FSMContext):
    await message.reply("Yaxshi")
    await state.update_data(lastname=message.text)    
    await message.answer("Telefon raqamingizni yuboring.", reply_markup=phone_markup)
    await state.set_state(FirstCupdownStates.phone)

async def get_phone_answer(message: Message, state: FSMContext):
    if message.contact:
        if message.contact.user_id == message.from_user.id:
            await message.reply("Yaxshi", reply_markup=ReplyKeyboardRemove())   
            await state.update_data(phone=message.contact.phone_number)

            await message.answer("Viloyatingnizni tanlang,", reply_markup=regions_markup)
            await state.set_state(FirstCupdownStates.region)
            return
    await message.answer("Pastdagi tugmaga bosish orqali telefon raqamingizni yuboring.", reply_markup=phone_markup)

async def get_school_answer(message: Message, state: FSMContext):
    await state.update_data(school=message.text)    
    await message.answer("Siz o'qituvchimisiz yoki o'quvchi?", reply_markup=select_job_markup)
    await state.set_state(FirstCupdownStates.job)

async def get_job_answer(message: Message, state: FSMContext):
    if message.text in ("O'qituvchi", "O'quvchi"):
        await state.update_data(job=message.text)
        if message.text == "O'quvchi":
            await message.answer("Nechanchi sinfda o'qiysiz?", reply_markup=class_button)
            await state.set_state(FirstCupdownStates.pupil_class)
        else:
            await message.answer("O'quvchingiz haqida ma'lumot yozing.\n\nNechanchi sinfligi va ism-familyasi", reply_markup=ReplyKeyboardRemove())
            await state.set_state(FirstCupdownStates.pupil_info)

async def get_pupil_class_answer(message: Message, state: FSMContext, bot: Bot):
    context = await state.get_data()
    ism = context.get("firstname")
    familya = context.get("lastname")
    telefon = context.get("phone")
    maktab = context.get("school")
    kimligi = context.get("job")
    sinfi = message.text
    viloyat = context.get("region_id")
    viloyat = get_region(viloyat)["name_uz"]
    tuman = context.get("district_id")
    tuman = get_district(tuman)["name_uz"]
    add_user(message.from_user.id, kimligi)
    add_pupil(
        message.from_user.id,
        ism,
        familya,
        telefon,
        viloyat,
        tuman,
        maktab,
        sinfi
    )
    await bot.send_message(
        chat_id=5165396993,
        text=f"""
🆕 YANGI O"QUVCHI:

ID: {message.from_user.id}
Ism: {ism}
Familya: {familya}
Telefon: {telefon}
Viloyat: {viloyat}
tuman: {tuman}
Maktab: {maktab}
Sinf: {sinfi}
"""
    )
    await message.answer("✅ Siz ro'yhatdan o'tdingiz!\n\nGuruh havolasi:\nhttps://t.me/+zCFMvEknhew4MWI6", reply_markup=ReplyKeyboardRemove())
    await state.clear()

async def get_pupil_info_answer(message: Message, state: FSMContext, bot: Bot):
    context = await state.get_data()
    ism = context.get("firstname")
    familya = context.get("lastname")
    telefon = context.get("phone")
    maktab = context.get("school")
    kimligi = context.get("job")
    pupil_info = message.text
    viloyat = context.get("region_id")
    viloyat = get_region(viloyat)["name_uz"]
    tuman = context.get("district_id")
    tuman = get_district(tuman)["name_uz"]
    add_user(message.from_user.id, kimligi)
    add_teacher(
        message.from_user.id,   
        ism,
        familya,
        telefon,
        viloyat,
        tuman,
        maktab,
        pupil_info
    )
    await bot.send_message(
        chat_id=5165396993,
        text=f"""
🆕 YANGI O"QITUVCHI:

ID: {message.from_user.id}
Ism: {ism}
Familya: {familya}
Telefon: {telefon}
Viloyat: {viloyat}
tuman: {tuman}
Maktab: {maktab}
Info: {pupil_info}
"""
    )
    await message.answer("✅ Siz ro'yhatdan o'tdingiz!\n\nGuruh havolasi:\nhttps://t.me/+zCFMvEknhew4MWI6", reply_markup=ReplyKeyboardRemove())
    await state.clear()
