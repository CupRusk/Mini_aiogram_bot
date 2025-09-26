# |-- IMPORTS_BASIC_BLOCK -------------------------------|
import asyncio
import os
from dotenv import load_dotenv
# -- IMPORT_AIOGRAM ---
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
# --- IMPORT_ROUTER ---
from routers.Cubic import router as cubic_router
from routers.echo_router import router as echo_router
from routers.say_hi import router as say_hi
from routers.about_bot import router as about_bot
from routers.cat import router as cat_router
# --- IMPORT_KEYBOARD ---
from keyboards import main_kb
# |------------------------------------------------------|

load_dotenv("token.env") 
token = os.getenv("TOKEN")

dp = Dispatcher()

@dp.message(Command("start"))
async def start(msg: Message):
    await msg.answer("Привет! Я мини проект на Aiogram",
                    reply_markup=main_kb)
    
print("Bot started")
dp.include_router(cat_router)
dp.include_router(about_bot)
dp.include_router(cubic_router)
dp.include_router(say_hi)
dp.include_router(echo_router)

async def main() -> None:
    bot = Bot(token=token)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main()) 