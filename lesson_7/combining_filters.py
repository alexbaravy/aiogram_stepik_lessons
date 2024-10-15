"""7.4 Фильтры
Комбинирование фильтров
https://stepik.org/lesson/891577/step/11?unit=896427"""

from environs import Env

import logging
import sys
import re

from aiogram import Bot, Dispatcher, F
from aiogram.filters import BaseFilter
from aiogram.types import Message

# Load environment variables
env = Env()
env.read_env()
bot_token = env('BOT_TOKEN')
user_id = env('USER_ID')

# Create bot and dispatcher instances
bot = Bot(token=bot_token)
dp = Dispatcher()


@dp.message(F.photo, F.from_user.id == int(user_id))  # AND
async def send_foto_by_admin(message: Message):
    await message.answer(text='This is photo from admin')


@dp.message(F.photo)
@dp.message(F.from_user.id == int(user_id))  # OR
async def send_foto_or_admin(message: Message):
    await message.answer(text='This is photo or admin')


@dp.message(F.from_user.id == ~int(user_id))  # OR and AND
async def send_not_photo(message: Message):
    await message.answer(text='This is voice or video from user')



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    dp.run_polling(bot)
