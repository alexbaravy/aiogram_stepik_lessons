from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
from keyboards import keyboard_utils
from user_data import users

# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    if message.from_user.id not in users:
        users[message.from_user.id] = {"total_games": 0, "wins": 0, "loses": 0, "draws": 0}
    await message.answer(text=LEXICON_RU['/start'])


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    if message.from_user.id not in users:
        users[message.from_user.id] = {"total_games": 0, "wins": 0, "loses": 0, "draws": 0}
    await message.answer(text=LEXICON_RU['/help'])


# Этот хэндлер срабатывает на команду /stat
@router.message(Command(commands='stat'))
async def process_stat_command(message: Message):
    if message.from_user.id not in users:
        users[message.from_user.id] = {"total_games": 0, "wins": 0, "loses": 0, "draws": 0}
    total_games = users[message.from_user.id]["total_games"]
    wins = users[message.from_user.id]["wins"]
    per_wins = round((wins / total_games * 100) if total_games > 0 else 0, 2)
    loses = users[message.from_user.id]["loses"]
    per_loses = round((loses / total_games * 100) if total_games > 0 else 0, 2)
    draws = total_games - wins - loses
    per_draws = (100 - per_wins - per_loses) if total_games > 0 else 0
    await message.answer(
        f'Всего игр сыграно: {total_games}\n'
        f'************************\n'
        f'Игр выиграно: {wins}\n'
        f'Игр вничью: {loses}\n'
        f'Игр проиграно: {draws}\n'
        f'************************\n'
        f'Процент побед: {per_wins}%\n'
        f'Процент проигрышей: {per_loses}%\n'
        f'Процент ничьих: {per_draws}%\n'
    )


# Этот хэндлер срабатывает на команду /play
@router.message(Command(commands='play'))
async def process_play_command(message: Message):
    if message.from_user.id not in users:
        users[message.from_user.id] = {"total_games": 0, "wins": 0, "loses": 0, "draws": 0}
    await message.answer(text=LEXICON_RU['/play'], reply_markup=keyboard_utils.rps_button(),
                         one_time_keyboard=True)
