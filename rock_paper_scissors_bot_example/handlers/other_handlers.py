import random

from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU
from user_data import users

# Инициализируем роутер уровня модуля
router: Router = Router()

choices = ['🗿', '📄', '✂️']
lose = ['✂️', '🗿', '📄']


# Этот хэндлер будет срабатывать на нажатие кнопок
@router.message(lambda message: message.text in choices)
async def send_button(message: Message):
    try:
        if message.from_user.id not in users:
            users[message.from_user.id] = {"total_games": 0, "wins": 0, "loses": 0, "draws": 0}
        computer_choice = random.choice(choices)
        await message.reply(computer_choice)
        index = choices.index(computer_choice)
        data = {'user_choice': message.text, 'computer_choice': computer_choice}
        users[message.from_user.id]['total_games'] += 1
        await message.answer(
            text=LEXICON_RU['bet_info'].format_map(data))
        if computer_choice == message.text:
            await message.answer(text=LEXICON_RU['draw'])
        elif lose[index] == message.text:
            await message.answer(text=LEXICON_RU['comp_win'])
        else:
            users[message.from_user.id]['wins'] += 1
            await message.answer(text=LEXICON_RU['you_win'])
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])

@router.message()
async def send_something(message:Message):
    await message.reply(text=LEXICON_RU['something'])

