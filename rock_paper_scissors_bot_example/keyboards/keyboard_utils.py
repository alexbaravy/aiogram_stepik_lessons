from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def rps_button():
    button_1 = KeyboardButton(text='🗿')
    button_2 = KeyboardButton(text='✂️')
    button_3 = KeyboardButton(text='📄')

    # Создаем объект клавиатуры, добавляя в него кнопки
    return ReplyKeyboardMarkup(keyboard=[[button_1, button_2, button_3]], resize_keyboard=True)
