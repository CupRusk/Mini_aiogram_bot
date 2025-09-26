from aiogram import F, Router
from aiogram.types import Message
import random
from study_aiogram.main import main_kb

router = Router()

router.message(F.text == "🎲 Кинуть кубик")
async def rand_num(msg: Message):
    number = random.randint(1, 6)
    responses = [
        f"Хей... У нас тут {number}! 😊",
        f"Выпало, {msg.from_user.first_name}!",
        f"Эй, {msg.from_user.first_name}, вот что выпало!"
    ]
    await msg.answer(random.choice(responses), reply_markup=main_kb)

