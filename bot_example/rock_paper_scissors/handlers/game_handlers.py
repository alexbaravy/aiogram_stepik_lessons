from aiogram import Router, F
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
from user_data import users
from services.services import get_bot_choice, get_winner

# Инициализируем роутер уровня модуля
router: Router = Router()

choices = [LEXICON_RU['rock'], LEXICON_RU['paper'], LEXICON_RU['scissors']]


# Этот хэндлер будет срабатывать на нажатие кнопок
@router.message(F.text.in_(choices))
async def game_buttons(message: Message):
    try:
        if message.from_user.id not in users:
            users[message.from_user.id] = {"total_games": 0, "wins": 0, "loses": 0, "draws": 0}
        bot_choice = get_bot_choice()
        await message.reply(bot_choice)
        data = {'user_choice': message.text, 'bot_choice': bot_choice}
        await message.answer(
            text=LEXICON_RU['bet_info'].format_map(data))
        winner = get_winner(message.from_user.id, message.text, bot_choice)
        await message.answer(text=LEXICON_RU[winner])

    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])
