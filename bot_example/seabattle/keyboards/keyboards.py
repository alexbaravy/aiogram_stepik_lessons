from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from services.services import FieldCallbackFactory
from lexicon.lexicon_ru import LEXICON_RU
from services.ships_generator import FIELD_SIZE
from user_data import users


# Функция, генерирующая клавиатуру в зависимости от данных из
# матрицы ходов пользователя
def get_field_keyboard(user_id: int) -> InlineKeyboardMarkup:
    array_buttons: list[list[InlineKeyboardButton]] = []

    for i in range(FIELD_SIZE):
        array_buttons.append([])
        for j in range(FIELD_SIZE):
            array_buttons[i].append(InlineKeyboardButton(
                text=LEXICON_RU[users[user_id]['field'][i][j]],
                callback_data=FieldCallbackFactory(x=i, y=j).pack()
            ))

    return InlineKeyboardMarkup(inline_keyboard=array_buttons)
