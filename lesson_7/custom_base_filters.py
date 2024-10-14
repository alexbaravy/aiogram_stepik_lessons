"""7.4 Фильтры
Собственные фильтры
https://stepik.org/lesson/891577/step/9?unit=896427
"""

from environs import Env

import logging
import sys

from aiogram import Bot, Dispatcher
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

# List of admin IDs
admin_ids: list[int] = [int(user_id)]


class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids


@dp.message(IsAdmin(admin_ids))
async def answer_if_admins_update(message: Message):
    await message.answer(text='You\'re Admin')


@dp.message()
async def answer_if_not_admins_update(message: Message):
    await message.answer(text='You\'re not Admin')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    dp.run_polling(bot)
