from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from lexicon.lexicon_ru import LEXICON_RU


def start_buttons():
    button_1 = KeyboardButton(text=LEXICON_RU['yes_button'])
    button_2 = KeyboardButton(text=LEXICON_RU['no_button'])
    button_3 = KeyboardButton(text=LEXICON_RU['help_button'])

    # Создаем объект клавиатуры, добавляя в него кнопки
    return ReplyKeyboardMarkup(keyboard=[[button_1, button_2, button_3]], resize_keyboard=True)


def game_buttons():
    button_1 = KeyboardButton(text=LEXICON_RU['rock'])
    button_2 = KeyboardButton(text=LEXICON_RU['scissors'])
    button_3 = KeyboardButton(text=LEXICON_RU['paper'])
    button_4 = KeyboardButton(text=LEXICON_RU['stat_button'])
    button_5 = KeyboardButton(text=LEXICON_RU['exit_button'])

    # Создаем объект клавиатуры, добавляя в него кнопки
    return ReplyKeyboardMarkup(keyboard=[[button_1, button_2, button_3], [button_4], [button_5]], resize_keyboard=True)
