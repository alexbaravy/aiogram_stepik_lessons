from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon_ru import LEXICON, DEFAULT_TEXT
from services.file_handling import book


def create_bookmarks_keyboard(*buttons: int) -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    for button in sorted(buttons):
        kb_builder.row(InlineKeyboardButton(
            text=f'{button} - {book[button][:100]}',
            callback_data=str(button)
        ))
    # Добавляем в клавиатуру в конце две кнопки "Редактировать" и "Отменить"
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON.get('edit_bookmarks_button', DEFAULT_TEXT),
            callback_data='edit_bookmarks'
        ),
        InlineKeyboardButton(
            text=LEXICON.get('cancel', DEFAULT_TEXT),
            callback_data='cancel'
        ),
        width=2
    )
    return kb_builder.as_markup()


def create_edit_keyboard(*buttons: int) -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    for button in sorted(buttons):
        kb_builder.row(InlineKeyboardButton(
            text=f'{LEXICON.get("del", DEFAULT_TEXT)} {button} - {book[button][:100]}',
            callback_data=f'{button}del'
        ))
    # Добавляем в конец клавиатуры кнопку "Отменить"
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON.get('cancel', DEFAULT_TEXT),
            callback_data='cancel'
        )
    )
    return kb_builder.as_markup()
