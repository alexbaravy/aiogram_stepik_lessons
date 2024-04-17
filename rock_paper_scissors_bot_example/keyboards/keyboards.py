from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def start_buttons():
    button_1 = KeyboardButton(text="Давай!")
    button_2 = KeyboardButton(text="Не хочу!")
    button_3 = KeyboardButton(text="Помощь")

    # Создаем объект клавиатуры, добавляя в него кнопки
    return ReplyKeyboardMarkup(keyboard=[[button_1, button_2, button_3]], resize_keyboard=True)


def game_buttons():
    button_1 = KeyboardButton(text='🗿')
    button_2 = KeyboardButton(text='✂️')
    button_3 = KeyboardButton(text='📄')
    button_4 = KeyboardButton(text='Статистика')
    button_5 = KeyboardButton(text='Выйти')

    # Создаем объект клавиатуры, добавляя в него кнопки
    return ReplyKeyboardMarkup(keyboard=[[button_1, button_2, button_3],[button_4],[button_5]], resize_keyboard=True)