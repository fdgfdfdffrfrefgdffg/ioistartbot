from aiogram import Router, F
from . import start, more, tasks
from filters import CheckUser, CheckSubChannels
from aiogram.enums import ChatType
from aiogram.filters import Command
from states import FirstCupdownStates
router = Router()

router.message.register(more.sub_channels_answer, CheckSubChannels())
router.message.register(start.start_answer, FirstCupdownStates.firstname)
router.message.register(start.get_lastname_answer, FirstCupdownStates.lastname)
router.message.register(start.get_phone_answer, FirstCupdownStates.phone)
router.message.register(start.get_school_answer, FirstCupdownStates.school)
router.message.register(start.get_job_answer, FirstCupdownStates.job)
router.message.register(start.get_pupil_class_answer, FirstCupdownStates.pupil_class)
router.message.register(start.get_pupil_info_answer, FirstCupdownStates.pupil_info)
router.message.register(start.first_cupdown_answer, CheckUser())
# router.message.register(tasks.send_task_details, Command("tasks"))
router.message.register(start.start_command_answer, Command("start"))
router.message.register(more.delete_user_answer, Command("del"))
router.message.register(more.send_db_file, F.text == "/senddb")
router.message.register(more.get_chat_id, F.text == "/id")
router.message.register(more.forward_msg, F.chat.type == ChatType.PRIVATE)