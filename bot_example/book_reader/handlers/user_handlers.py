import logging

from functools import wraps
from enum import Enum

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message


from filters.filters import IsDelBookmarkCallbackData, IsDigitCallbackData
from keyboards.bookmarks_kb import (create_bookmarks_keyboard,
                                    create_edit_keyboard)
from keyboards.pagination_kb import create_pagination_keyboard
from lexicon.lexicon_ru import LEXICON, DEFAULT_TEXT

from services.user_manager import UserManager
from services.file_handling import book

# Инициализируем логгер
logger = logging.getLogger(__name__)

router = Router()

class PageDirection(Enum):
    FORWARD = 'forward'
    BACKWARD = 'backward'


def log_function_call(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        logger.info(f"START {func.__name__}")
        try:
            result = await func(*args, **kwargs)
            return result
        finally:
            logger.info(f"FINISH {func.__name__}")

    return wrapper


# Инициализация UserManager
user_manager = UserManager()

# Функция пагинации клавиатуры
def get_pagination_keyboard(user_id: int):
    page_info = f'{user_manager.get_user_page(user_id)}/{len(book)}'
    return create_pagination_keyboard(PageDirection.BACKWARD.value, page_info, PageDirection.FORWARD.value)


# /start
@router.message(CommandStart())
@log_function_call
async def process_start_command(message: Message):
    user_manager.ensure_user_exists(message.from_user.id)
    await message.answer(LEXICON.get(message.text, DEFAULT_TEXT))


# /help
@router.message(Command(commands='help'))
@log_function_call
async def process_help_command(message: Message):
    user_manager.ensure_user_exists(message.from_user.id)
    await message.answer(LEXICON.get(message.text, DEFAULT_TEXT))


# /beginning - отправлять пользователю первую страницу книги с кнопками пагинации
@router.message(Command(commands='beginning'))
@log_function_call
async def process_beginning_command(message: Message):
    text = book[user_manager.reset_user_page(message.from_user.id)]
    reply_markup = get_pagination_keyboard(message.from_user.id)
    await message.answer(text=text, reply_markup=reply_markup)


# /continue - отправлять пользователю страницу книги, на которой пользователь остановился
@router.message(Command(commands='continue'))
@log_function_call
async def process_continue_command(message: Message):
    text = book[user_manager.get_user_page(message.from_user.id)]
    reply_markup = get_pagination_keyboard(message.from_user.id)
    await message.answer(text=text, reply_markup=reply_markup)


# /bookmarks - список закладок
@router.message(Command(commands='bookmarks'))
@log_function_call
async def process_bookmarks_command(message: Message):
    bookmarks = user_manager.get_user_bookmarks(message.from_user.id)
    if bookmarks:
        await message.answer(
            text=LEXICON.get(message.text, DEFAULT_TEXT),
            reply_markup=create_bookmarks_keyboard(*bookmarks)
        )
    else:
        await message.answer(text=LEXICON.get('no_bookmarks', DEFAULT_TEXT))


# Функция для обработки хэндлеров "вперед" и "назад"
async def update_message_page(callback: CallbackQuery, page_direction: PageDirection):
    user_id = callback.from_user.id
    current_page = user_manager.get_user_page(user_id)
    book_length = len(book)
    if page_direction == PageDirection.FORWARD:
        if current_page >= book_length:
            await callback.answer(LEXICON.get('last_page', DEFAULT_TEXT))
            return
        current_page = user_manager.change_user_page(user_id, 1)
    elif page_direction == PageDirection.BACKWARD:
        if current_page <= 1:
            await callback.answer(LEXICON.get('first_page', DEFAULT_TEXT))
            return
        current_page = user_manager.change_user_page(user_id, -1)

    text = book[current_page]
    reply_markup = get_pagination_keyboard(user_id)
    await callback.message.edit_text(text=text, reply_markup=reply_markup)


# Листать "Вперед"
@router.callback_query(F.data == PageDirection.FORWARD.value)
@log_function_call
async def process_forward_press(callback: CallbackQuery):
    await update_message_page(callback, PageDirection.FORWARD)


# Листать "Назад"
@router.callback_query(F.data == PageDirection.BACKWARD.value)
@log_function_call
async def process_backward_press(callback: CallbackQuery):
    await update_message_page(callback, PageDirection.BACKWARD)


# Добавить в закладки
@router.callback_query(lambda x: '/' in x.data and x.data.replace('/', '').isdigit())
@log_function_call
async def process_page_press(callback: CallbackQuery):
    user_id = callback.from_user.id
    bookmarks = user_manager.get_user_bookmarks(user_id)
    current_page = user_manager.get_user_page(user_id)
    bookmarks.add(current_page)

    await callback.answer(LEXICON.get('added_bookmarks', DEFAULT_TEXT))


# Перейти по закладке
@router.callback_query(IsDigitCallbackData())
@log_function_call
async def process_bookmark_press(callback: CallbackQuery):
    user_id = callback.from_user.id
    page = int(callback.data)
    user_manager.go_bookmark(user_id, page)
    text = book[page]
    reply_markup = get_pagination_keyboard(user_id)
    await callback.message.edit_text(text=text, reply_markup=reply_markup)


# Редактировать закладки
@router.callback_query(F.data == 'edit_bookmarks')
@log_function_call
async def process_edit_press(callback: CallbackQuery):
    user_id = callback.from_user.id
    bookmarks = user_manager.get_user_bookmarks(user_id)
    await callback.message.edit_text(
        text=LEXICON.get(callback.data, DEFAULT_TEXT),
        reply_markup=create_edit_keyboard(*bookmarks)
    )


# Отменить в Закладках
@router.callback_query(F.data == 'cancel')
@log_function_call
async def process_cancel_press(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON.get('cancel_text', DEFAULT_TEXT))


# Удалить закладку
@router.callback_query(IsDelBookmarkCallbackData())
@log_function_call
async def process_del_bookmark_press(callback: CallbackQuery):
    user_id = callback.from_user.id
    page_to_remove = int(callback.data[:-3])
    bookmarks = user_manager.get_user_bookmarks(user_id)
    bookmarks.discard(page_to_remove)

    if bookmarks:
        await callback.message.edit_text(
            text=LEXICON.get('/bookmarks', DEFAULT_TEXT),
            reply_markup=create_edit_keyboard(*bookmarks)
        )
    else:
        await callback.message.edit_text(text=LEXICON.get('no_bookmarks', DEFAULT_TEXT))