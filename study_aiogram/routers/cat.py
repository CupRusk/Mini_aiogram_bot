from aiogram import Router, F
from aiogram.types import Message
from keyboards import main_kb
from aiogram.exceptions import TelegramBadRequest
import random
import aiohttp

router = Router()

cat_urls = [
    "https://media.istockphoto.com/id/1285744732/ro/fotografie/pisica-ro%C8%99ie-st%C3%A2nd-lateral-%C8%99i-privind-transformat%C4%83-%C3%AEn-camer%C4%83-izolat-pe-alb.webp?s=2048x2048&w=is&k=20&c=A87eASFJa0raNnWOeXpULIbPmwyc0zCFDldCpXC5J9Y=",
]

@router.message(F.text == "🐱 Показать котика")
async def send_cat(msg: Message):
    try:
        print("Cat command triggered")
        await msg.answer_photo(
            photo=random.choice(cat_urls),
            caption="Вот твой котик! 🐱",
            reply_markup=main_kb
        )
    except Exception as e:
        print(f"Error sending cat: {e}")
        await msg.answer("Извините, не удалось загрузить котика 😿", reply_markup=main_kb)