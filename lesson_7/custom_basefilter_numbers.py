"""7.4 Фильтры
Передача аргументов в хэндлеры из фильтров
https://stepik.org/lesson/891577/step/10?unit=896427
"""

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

# Create bot and dispatcher instances
bot = Bot(token=bot_token)
dp = Dispatcher()


class NumbersInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        """Extract all numbers from the message text"""
        numbers = list(map(int, re.findall(r'\d+', message.text)))

        return {'numbers': numbers} if numbers else False


@dp.message(F.text.lower().startswith('найди числа'), NumbersInMessage())
async def process_if_numbers(message: Message, numbers: list[int]):
    await message.answer(text=f'Нашел: {", ".join(str(num) for num in numbers)}')


@dp.message(F.text.lower().startswith('найди числа'))
async def process_if_not_numbers(message: Message):
    await message.answer(text='Не нашел что-то :(')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    dp.run_polling(bot)
