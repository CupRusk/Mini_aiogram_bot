from aiogram import F, Router 
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
import asyncio
from study_aiogram.main import main_kb

router = Router()

@router.message(F.text)
async def echo(msg: Message):
    await msg.answer(f"Ты ввёл {msg.text}", reply_markup=main_kb)