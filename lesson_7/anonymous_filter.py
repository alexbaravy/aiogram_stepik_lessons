"""7.4 Фильтры
Напишите функцию anonymous_filter, используя синтаксис анонимных функций, которая принимает строковый аргумент и
возвращает значение True, если количество русских букв я не меньше 23 (регистр буквы неважен) и False в противном
случае."""

import re
from environs import Env

import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

# Load environment variables
env = Env()
env.read_env()
bot_token = env('BOT_TOKEN')

# Create bot and dispatcher instances
bot = Bot(token=bot_token)
dp = Dispatcher()


def anonymous_filter(message: Message) -> bool:
    """Check if the message contains at least 23 occurrences of the letter 'я'."""
    return len(re.findall('[я]', message.text.lower())) >= 23
    # return sum(1 for char in message.text.lower() if char == 'я') >= 23


@dp.message(Command(commands="start"))
async def process_start_command(message: Message):
    """Handle /start command."""
    await message.answer("Введите любую текстовую строку")


@dp.message(anonymous_filter)
async def anonymous_filter(message: Message):
    """Handle messages that pass the anonymous filter."""
    await message.answer("Ваше сообщение содержит 23 или более 'я'.")


@dp.message()
async def other_result(message: Message):
    """Handle messages that do not pass the anonymous filter."""
    await message.answer("Ваше сообщение содержит менее 23 'я'.")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    dp.run_polling(bot)