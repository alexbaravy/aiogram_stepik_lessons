from aiogram import Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from lexicon.lexicon_ru import LEXICON_RU
from services.services import FieldCallbackFactory, reset_field
from keyboards.keyboards import get_field_keyboard
from user_data import users

# Инициализируем роутер уровня модуля
router: Router = Router()

# Этот хэндлер будет срабатывать на команду /start, записывать
# пользователя в "базу данных", обнулять игровое поле и отправлять
# пользователю сообщение с клавиатурой
@router.message(CommandStart())
async def process_start_command(message: Message):
    if message.from_user.id not in users:
        users[message.from_user.id] = {}
    reset_field(message.from_user.id)
    await message.answer(
        text=LEXICON_RU['/start'],
        reply_markup=get_field_keyboard(message.from_user.id)
    )

# Этот хэндлер будет срабатывать на нажатие любой инлайн-кнопки на поле,
# запускать логику проверки результата нажатия и формирования ответа
@router.callback_query(FieldCallbackFactory.filter())
async def process_category_press(callback: CallbackQuery,
                                 callback_data: FieldCallbackFactory):
    field = users[callback.from_user.id]['field']
    ships = users[callback.from_user.id]['ships']
    if field[callback_data.x][callback_data.y] == 0 and \
    ships[callback_data.x][callback_data.y] == 0:
        answer = LEXICON_RU['miss']
        field[callback_data.x][callback_data.y] = 1
    elif field[callback_data.x][callback_data.y] == 0 and \
    ships[callback_data.x][callback_data.y] == 1:
        answer = LEXICON_RU['hit']
        field[callback_data.x][callback_data.y] = 2
    else:
        answer = LEXICON_RU['used']

    try:
        await callback.message.edit_text(
            text=LEXICON_RU['next_move'],
            reply_markup=get_field_keyboard(callback.from_user.id)
        )
    except TelegramBadRequest:
        pass

    await callback.answer(answer)