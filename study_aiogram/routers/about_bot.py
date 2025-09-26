from aiogram import Router, F
from aiogram.types import Message
from study_aiogram.main import main_kb
import random
router = Router()

@router.message(F.text == "📖 О боте")
async def about_bot(msg: Message):
    random_num = random.randint(1, 10)
    responses = [
        "Я бот, созданный с помощью Aiogram. Могу кидать кубики и приветствовать тебя!",
        "Этот бот написан на Python с использованием библиотеки Aiogram.",
        "Я простой бот, который любит общаться и играть с кубиками!"
    ]
    if random_num > 7:
        responses.append("Хм... в чём смысл жизни? Может быть, в общении с ботами?")
        
    await msg.answer(random.choice(responses),
                reply_markup=main_kb)