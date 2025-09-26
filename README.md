# Mini Aiogram Bot

A modular Telegram bot built with [Aiogram 3](https://docs.aiogram.dev/) and Python 3.13.  
Designed as a learning project to demonstrate command handling, custom keyboards, modular routers, and environment-based configuration.

## Features
- `/start` command with main menu
- Modular routers for different functionalities:
  - About bot
  - Dice rolling
  - Greeting users
  - Cat images
- Randomized responses and light “Easter eggs”
- Clean structure with `.env` for token security
- Reply keyboard with intuitive interface

## Structura
```
study_aiogram/
├── routers/
│   ├── about_bot.py
│   ├── cat.py
│   ├── Cubic.py
│   ├── echo_router.py
│   └── say_hi.py
├── keyboards.py
├── main.py
├── setup.sh
├── token.env (ignored by git)
└── README.md
```

## Installation

```bash
git clone https://github.com/yourusername/mini-aiogram-bot.git
cd mini-aiogram-bot
chmod +x setup.sh
./setup.sh
source .venv/bin/activate
```
