from environs import Env
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery

# Инициализируем логгер
logger = logging.getLogger(__name__)

# Конфигурируем логирование
logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)d #%(levelname)-8s '
           '[%(asctime)s] - %(name)s - %(message)s')

env = Env()  # Создаем экземпляр класса Env
env.read_env()  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
bot_token = env('BOT_TOKEN')  # Получаем и сохраняем значение переменной окружения в переменную bot_token

# Создаем объекты бота и диспетчера
bot = Bot(token=bot_token)
dp = Dispatcher()

# Создаем объекты инлайн-кнопок
big_button_1 = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 1',
    callback_data='big_button_1_pressed'
)

big_button_2 = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 2',
    callback_data='big_button_2_pressed'
)

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_1],
                     [big_button_2]]
)


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру с инлайн-кнопками
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Это инлайн-кнопки. Нажми на любую!',
        reply_markup=keyboard
    )


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_1_pressed'
@dp.callback_query(F.data == 'big_button_1_pressed')
async def process_button_1_press(callback: types.CallbackQuery):
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 2':
        await callback.message.edit_text(
            text='Была нажата БОЛЬШАЯ КНОПКА 1',
            reply_markup=callback.message.reply_markup
        )
    await callback.answer(text='Ура! Нажата кнопка 1', show_alert=True)


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_2_pressed'
@dp.callback_query(F.data == 'big_button_2_pressed')
async def process_button_2_press(callback: types.CallbackQuery):
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 2':
        await callback.message.edit_text(
            text='Была нажата БОЛЬШАЯ КНОПКА 2',
            reply_markup=callback.message.reply_markup
        )
    await callback.answer(text='Ура! Нажата кнопка 2', show_alert=True)


# # Обработчик для нажатия на инлайн-кнопки
# @dp.callback_query(lambda query: True)
# async def process_callback_button(query: types.CallbackQuery):
#     # Выводим в лог информацию о нажатой кнопке
#     logger.info(f'Button "{query.data}" pressed by user {query.from_user.id}')
#
#     # Здесь вы можете изучить структуру апдейта
#     logger.info(f'Update structure: {query}')
#
#     # Дополнительные действия с данными из апдейта
#     await query.answer('Вы нажали на кнопку!')
#
#     # Ответ бота на нажатие кнопки (необязательно)
#     # await bot.send_message(query.from_user.id, 'Вы нажали на кнопку!')


if __name__ == '__main__':
    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')
    dp.run_polling(bot)
