#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate
pip install aiogram python-dotenv
touch token.env
echo "TOKEN=your_bot_token" >> token.env
echo "Setup complete. Please edit token.env to add your bot token!"