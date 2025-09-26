# |-- IMPORTS_BASIC_BLOCK -------------------------------|
import asyncio
import random
import os
from dotenv import load_dotenv
# -- IMPORT_AIOGRAM ---
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# --- IMPORT_ROUTER ---
from study_aiogram.routers.Cubic import router as cubic_router
from study_aiogram.routers.echo_router import router as echo_router
from study_aiogram.routers.say_hi import router as say_hi
from study_aiogram.routers.about_bot import router as about_bot
from study_aiogram.keyboard import main_kb
# |------------------------------------------------------|

load_dotenv("token.env") 
token = os.getenv("TOKEN")

dp = Dispatcher()

@dp.message(Command("start"))
async def start(msg: Message):
    await msg.answer("Привет! Я мини проект на Aiogram",
                    reply_markup=main_kb)

dp.include_router(about_bot)
dp.include_router(say_hi)
dp.include_router(cubic_router)
dp.include_router(echo_router)

async def main() -> None:
    bot = Bot(token=token)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main()) 