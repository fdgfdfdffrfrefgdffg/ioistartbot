from aiogram import Router, F
from . import signup
from . import more
from states import FirstCupdownStates

router = Router()

router.callback_query.register(signup.get_region_answer, FirstCupdownStates.region)
router.callback_query.register(signup.get_district_answer, FirstCupdownStates.district)
router.callback_query.register(more.sub_channels_answer, F.data == "checksub")