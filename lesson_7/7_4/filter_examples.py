"""7.4 Фильтры"""

from dataclasses import dataclass, field
from environs import Env

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

# Load environment variables
env = Env()
env.read_env()
bot_token = env('BOT_TOKEN')

# Create bot and dispatcher instances
bot = Bot(token=bot_token)
dp = Dispatcher()


@dataclass
class AdminList:
    id: dict[str, int] = field(default_factory=dict)


admin_list = AdminList()
admin_list.id['baa'] = 6165145864


def my_admin_filter(message: Message) -> bool:
    return message.text == '/admin' and message.from_user.id in admin_list.id.values()


@dp.message(Command(commands='start'))
async def process_start_command(message: Message):
    """Handle /start command."""
    await message.answer(text='Это команда /start')


@dp.message(my_admin_filter)
async def process_admin_command(message: Message):
    """Handle /admin command."""
    await message.answer(text='Это команда /admin')
    print(message.from_user)


if __name__ == '__main__':
    dp.run_polling(bot)
