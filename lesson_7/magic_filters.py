"""7.4 Фильтры
Magic filters
https://docs.aiogram.dev/en/dev-3.x/dispatcher/filters/magic_filters.html#magic-filters
"""

import re
from environs import Env

import logging
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message


# Load environment variables
env = Env()
env.read_env()
bot_token = env('BOT_TOKEN')

# Create bot and dispatcher instances
bot = Bot(token=bot_token)
dp = Dispatcher()


@dp.message(F.from_user.id == 6165145864)
async def send_message(message: Message):
    print(message)
    await message.answer(text=f'Message from {message.from_user.id}')

@dp.message()
async def send_other_message(message: Message):
    print(message)
    await message.answer(text=f'Message from {message.from_user.first_name}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    dp.run_polling(bot)
