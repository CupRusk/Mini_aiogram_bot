from aiogram import Router, F
from aiogram.types import Message
from keyboards import main_kb
import random

router = Router()

@router.message(F.text == "📖 О боте")
async def about_bot(msg: Message):
    responses = [
        "Привет! Я бот на Aiogram, умею кидать кубики и говорить привет 😎",
        "Я — твой маленький помощник на Python, готов развлекать и общаться!",
        "Простой бот, который любит игры, шутки и немного философии 🌀",
        "Скажем прямо, я бот… но зато весёлый! 🎲👋",
        "Привет-привет! Давай вместе бросим кубик или просто поболтаем 😉"
    ]
    
    if random.randint(1, 10) > 7:
        responses.append("Иногда я думаю… может, смысл жизни в том, чтобы кидать кубики и общаться? 🤔")
        
    await msg.answer(random.choice(responses), reply_markup=main_kb)
