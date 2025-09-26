from aiogram import Router, F
from aiogram.types import Message
from study_aiogram.main import main_kb
import random

router = Router()

@router.message(F.text == "👋 Сказать привет")
async def echo_hi(msg: Message):
    responses = [
        f"Привет, {msg.from_user.first_name}! 😊",
        f"Хай-хай, {msg.from_user.first_name}!",
        f"Эй, {msg.from_user.first_name}, рад тебя видеть!"
    ]
    await msg.answer(random.choice(responses), reply_markup=main_kb)