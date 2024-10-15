""" 7.3 Бот "Угадай число" """

import logging
import sys
import random
from environs import Env
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

# Load environment variables
env = Env()
env.read_env()
bot_token = env('BOT_TOKEN')

# Create bot and dispatcher instances
bot = Bot(bot_token)
dp = Dispatcher()

# Constants
ATTEMPTS = 5

# User data structure
users = {}


def get_random_number() -> int:
    """Returns a random integer between 1 and 100."""
    return random.randint(1, 100)


def initialize_user(user_id):
    """Initialize user data in the users dictionary."""
    users[user_id] = {
        'in_game': False,
        'secret_number': None,
        'attempts': 0,
        'total_games': 0,
        'wins': 0
    }


@dp.message(CommandStart())
async def process_start_command(message: Message):
    """Handle /start command."""
    await message.answer(
        'Привет!\nДавайте сыграем в игру "Угадай число"?\n\n'
        'Чтобы получить правила игры и список доступных команд - отправьте команду /help'
    )
    if message.from_user.id not in users:
        initialize_user(message.from_user.id)


@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    """Handle /help command."""
    await message.answer(
        f'Правила игры:\n\n'
        f'Я загадываю число от 1 до 100, а вам нужно его угадать\n'
        f'У вас есть {ATTEMPTS} попыток\n\n'
        f'Доступные команды:\n'
        f'/help - правила игры и список команд\n'
        f'/cancel - выйти из игры\n'
        f'/stat - посмотреть статистику\n\n'
        f'Давай сыграем?'
    )


@dp.message(Command(commands='stat'))
async def process_stat_command(message: Message):
    """Handle /stat command."""
    user_stats = users[message.from_user.id]
    await message.answer(
        f'Всего игр сыграно: {user_stats["total_games"]}\n'
        f'Игр выиграно: {user_stats["wins"]}'
    )


@dp.message(Command(commands='cancel'))
async def process_cancel_command(message: Message):
    """Handle /cancel command."""
    user = users[message.from_user.id]
    if user['in_game']:
        user['in_game'] = False
        await message.answer('Вы вышли из игры. Если захотите сыграть снова - напишите об этом')
    else:
        await message.answer('А мы и так с вами не играем. Может, сыграем разок?')


@dp.message(F.text.lower().in_(['да', 'давай', 'сыграем', 'игра', 'играть', 'хочу играть']))
async def process_positive_answer(message: Message):
    """Handle positive responses to play the game."""
    user = users[message.from_user.id]
    if not user['in_game']:
        user['in_game'] = True
        user['secret_number'] = get_random_number()
        user['attempts'] = ATTEMPTS
        await message.answer('Ура!\n\nЯ загадал число от 1 до 100, попробуй угадать!')
    else:
        await message.answer(
            'Пока мы играем в игру я могу реагировать только на числа от 1 до 100 и команды /cancel и /stat')


@dp.message(F.text.lower().in_(['нет', 'не', 'не хочу', 'не буду']))
async def process_negative_answer(message: Message):
    """Handle negative responses to play the game."""
    user = users[message.from_user.id]
    if not user['in_game']:
        await message.answer('Жаль :(\n\nЕсли захотите поиграть - просто напишите об этом')
    else:
        await message.answer('Мы же сейчас с вами играем. Присылайте, пожалуйста, числа от 1 до 100')


@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def process_numbers_answer(message: Message):
    """Handle number guesses from the user."""
    user = users[message.from_user.id]
    if user['in_game']:
        user_guess = int(message.text)
        if user_guess == user['secret_number']:
            user['in_game'] = False
            user['total_games'] += 1
            user['wins'] += 1
            await message.answer('Ура!!! Вы угадали число!\n\nМожет, сыграем еще?')
        else:
            user['attempts'] -= 1
            hint = 'меньше' if user_guess > user['secret_number'] else 'больше'
            await message.answer(f'Мое число {hint}')

        if user['attempts'] == 0:
            user['in_game'] = False
            user['total_games'] += 1
            await message.answer(
                f'К сожалению, у вас больше не осталось попыток. Вы проиграли :(\n\n'
                f'Мое число было {user["secret_number"]}\n\n'
                f'Давайте сыграем еще?'
            )
    else:
        await message.answer('Мы еще не играем. Хотите сыграть?')


@dp.message()
async def process_other_answers(message: Message):
    """Handle any other messages."""
    user = users[message.from_user.id]
    if user['in_game']:
        await message.answer('Мы же сейчас с вами играем. Присылайте, пожалуйста, числа от 1 до 100')
    else:
        await message.answer('Я довольно ограниченный бот, давайте просто сыграем в игру?')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    dp.run_polling(bot)