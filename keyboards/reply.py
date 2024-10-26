from aiogram.utils.keyboard import ReplyKeyboardBuilder

phone_markup = ReplyKeyboardBuilder()
phone_markup.button(text="Telefon raqamni yuborish", request_contact=True)
phone_markup = phone_markup.as_markup()
phone_markup.resize_keyboard = True
phone_markup.is_persistent = True

select_job_markup = ReplyKeyboardBuilder()
select_job_markup.button(text="O'qituvchi")
select_job_markup.button(text="O'quvchi")
select_job_markup.adjust(2)
select_job_markup = select_job_markup.as_markup()
select_job_markup.resize_keyboard = True
select_job_markup.is_persistent = True

class_button = ReplyKeyboardBuilder()
class_button.button(text="9")
class_button.button(text="10")
class_button.button(text="11")
class_button = class_button.as_markup()
class_button.resize_keyboard = True
class_button.is_persistent = True