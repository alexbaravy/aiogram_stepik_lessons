import random

from lexicon.lexicon_ru import LEXICON_RU
from user_data import users


# Функция, возвращающая случайный выбор бота в игре
def get_bot_choice() -> str:
    return random.choice([LEXICON_RU['rock'], LEXICON_RU['paper'], LEXICON_RU['scissors']])


# Функция, возвращающая ключ из словаря, по которому
# хранится значение, передаваемое как аргумент - выбор пользователя
def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            break
    return key


# Функция, определяющая победителя
def get_winner(user_id, user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    bot_choice = _normalize_user_answer(bot_choice)
    rules = {'rock': 'scissors',
             'scissors': 'paper',
             'paper': 'rock'}
    users[user_id]['total_games'] += 1
    if user_choice == bot_choice:
        users[user_id]['draws'] += 1
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        users[user_id]['wins'] += 1
        return 'user_won'
    users[user_id]['loses'] += 1
    return 'bot_won'
