from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📖 О боте")],
        [KeyboardButton(text="🎲 Кинуть кубик")],
        [KeyboardButton(text="👋 Сказать привет")],
        [KeyboardButton(text="🐱 Показать котика")]
    ],
    resize_keyboard=True
)