"""7.4 Фильтры
Немного о content_type
https://docs.aiogram.dev/en/dev-3.x/api/enums/content_type.html#module-aiogram.enums.content_type
"""

import re
from environs import Env

import logging
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ContentType
from aiogram.filters import Command

# Load environment variables
env = Env()
env.read_env()
bot_token = env('BOT_TOKEN')

# Create bot and dispatcher instances
bot = Bot(token=bot_token)
dp = Dispatcher()


@dp.message(F.content_type == ContentType.PHOTO)
# @dp.message(F.content_type == 'photo')
# @dp.message(F.photo)
async def process_send_photo(message: Message):
    await message.answer(text='This is Photo')


@dp.message(F.content_type.in_({'voice', 'video', 'text'}))
# @dp.message(F.content_type.in_({ContentType.VOICE,ContentType.VIDEO,ContentType.TEXT}))
async def process_send_vovite(message: Message):
    await message.answer(text='This is voice or video or text')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    dp.run_polling(bot)
