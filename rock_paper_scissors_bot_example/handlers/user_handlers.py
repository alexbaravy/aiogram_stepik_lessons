from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, CommandStart

from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboards import start_buttons, game_buttons
from user_data import users

# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    if message.from_user.id not in users:
        users[message.from_user.id] = {"total_games": 0, "wins": 0, "loses": 0, "draws": 0}
    await message.answer(text=LEXICON_RU['start'], reply_markup=start_buttons(),
                         one_time_keyboard=True)


# Этот хэндлер срабатывает на кнопку help_button
@router.message(F.text == LEXICON_RU['help_button'])
async def process_help_command(message: Message):
    if message.from_user.id not in users:
        users[message.from_user.id] = {"total_games": 0, "wins": 0, "loses": 0, "draws": 0}
    await message.answer(text=LEXICON_RU['help'])


# Этот хэндлер срабатывает на кнопку stat_button
@router.message(F.text == LEXICON_RU['stat_button'])
async def process_stat_command(message: Message):
    if message.from_user.id not in users:
        users[message.from_user.id] = {"total_games": 0, "wins": 0, "loses": 0, "draws": 0}
    total_games = users[message.from_user.id]["total_games"]

    wins = users[message.from_user.id]["wins"]
    draws = users[message.from_user.id]["draws"]
    loses = users[message.from_user.id]["loses"]

    per_wins = round((wins / total_games * 100) if total_games > 0 else 0, 2)
    per_draws = round((draws / total_games * 100) if total_games > 0 else 0, 2)
    per_loses = round((loses / total_games * 100) if total_games > 0 else 0, 2)

    data = {
        'total_games': total_games,
        'wins': wins, 'draws': draws,
        'loses': loses,
        'per_wins': per_wins,
        'per_draws': per_draws,
        'per_loses': per_loses
    }

    await message.answer(text=LEXICON_RU['stat'].format_map(data))


# Этот хэндлер срабатывает на yes_button
@router.message(F.text == LEXICON_RU['yes_button'])
async def process_play_command(message: Message):
    if message.from_user.id not in users:
        users[message.from_user.id] = {"total_games": 0, "wins": 0, "loses": 0, "draws": 0}
    await message.answer(text=LEXICON_RU['play'], reply_markup=game_buttons(),
                         one_time_keyboard=True)


# Этот хэндлер срабатывает на команду no_button
@router.message(F.text.in_([LEXICON_RU['no_button'], LEXICON_RU['exit_button']]))
async def process_play_command(message: Message):
    await message.answer(text=LEXICON_RU['stop'],
                         reply_markup=ReplyKeyboardRemove())


@router.message(Command(commands='allstat'))
async def process_play_command(message: Message):
    await message.answer(text=str(users))
