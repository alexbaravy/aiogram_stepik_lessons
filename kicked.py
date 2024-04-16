import os
from environs import Env

import logging
import sys

from aiogram.filters import ChatMemberUpdatedFilter, KICKED
from aiogram.types import ChatMemberUpdated
from aiogram import Bot, Dispatcher

env = Env()  # Создаем экземпляр класса Env
env.read_env()  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
bot_token = env('BOT_TOKEN')  # Получаем и сохраняем значение переменной окружения в переменную bot_token

# Создаем объекты бота и диспетчера
bot = Bot(token=bot_token)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на блокировку бота пользоif __name__ == '__main__':
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     dp.run_polling(bot)вателем
@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def process_user_blocked_bot(event: ChatMemberUpdated):
    print(f'Пользователь {event.from_user.id} заблокировал бота')

# Если запустить бота с таким хэндлером и затем заблокировать бота в клиенте, то в терминале увидим:
# Пользователь XXXXXXXXX заблокировал бота

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    dp.run_polling(bot)