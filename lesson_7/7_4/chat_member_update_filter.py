"""7.4 Фильтры
ChatMemberUpdatedFilter
https://docs.aiogram.dev/en/dev-3.x/dispatcher/filters/chat_member_updated.html
"""

import re
from environs import Env

import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.types import ChatMemberUpdated
from aiogram.filters import ChatMemberUpdatedFilter, KICKED

# Load environment variables
env = Env()
env.read_env()
bot_token = env('BOT_TOKEN')

# Create bot and dispatcher instances
bot = Bot(token=bot_token)
dp = Dispatcher()


@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def process_user_blocked_bot(event: ChatMemberUpdated):
    print(f'User {event.from_user.id} blocked bot')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    dp.run_polling(bot)
