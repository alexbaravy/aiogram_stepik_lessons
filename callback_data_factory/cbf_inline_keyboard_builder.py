from environs import Env
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

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


# Создаем свой класс фабрики коллбэков, указывая префикс
class GoodsCallbackFactory(CallbackData, prefix='goods', sep='|'):
    category_id: int
    subcategory_id: int
    item_id: int


# Инициализируем билдер инлайн-клавиатуры
builder = InlineKeyboardBuilder()

# Добавляем первую кнопку в билдер
builder.button(
    text='Категория 1',
    callback_data=GoodsCallbackFactory(
        category_id=1,
        subcategory_id=0,
        item_id=0
    )
)

list_cat = [{'text': 'Категория 1', 'category_id': 1, 'subcategory_id': 3, 'item_id': 7},
            {'text': 'Категория 2', 'category_id': 2, 'subcategory_id': 5, 'item_id': 1},
            {'text': 'Категория 3', 'category_id': 3, 'subcategory_id': 2, 'item_id': 8},
            {'text': 'Категория 4', 'category_id': 4, 'subcategory_id': 1, 'item_id': 5},
            {'text': 'Категория 5', 'category_id': 5, 'subcategory_id': 0, 'item_id': 6},
            {'text': 'Категория 6', 'category_id': 6, 'subcategory_id': 4, 'item_id': 10},
            {'text': 'Категория 7', 'category_id': 7, 'subcategory_id': 3, 'item_id': 9},
            {'text': 'Категория 8', 'category_id': 8, 'subcategory_id': 2, 'item_id': 3},
            {'text': 'Категория 9', 'category_id': 9, 'subcategory_id': 1, 'item_id': 4},
            {'text': 'Категория 10', 'category_id': 10, 'subcategory_id': 5, 'item_id': 2}]


for category in list_cat:
    builder.button(
        text=category['text'],
        callback_data=GoodsCallbackFactory(
            category_id=category['category_id'],
            subcategory_id=category['subcategory_id'],
            item_id=category['item_id']
        )
    )


# Этот хэндлер будет срабатывать на команду /start
# и отправлять пользователю сообщение с клавиатурой
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Вот такая клавиатура',
        reply_markup=builder.as_markup()
    )


# Этот хэндлер будет срабатывать на нажатие любой
# инлайн кнопки и распечатывать апдейт в терминал
@dp.callback_query(GoodsCallbackFactory.filter())
async def process_any_inline_button_press(callback: CallbackQuery, callback_data: GoodsCallbackFactory):
    print(callback.model_dump_json(indent=4, exclude_none=True))
    await callback.message.answer(text=f'Категория товаров: {callback_data.category_id}\n'
                                       f'Подкатегория товаров: {callback_data.subcategory_id}\n'
                                       f'Товар: {callback_data.item_id}\n'
                                  )
    await callback.answer()


# Сообщаем билдеру схему размещения кнопок (здесь по одной в ряду)
builder.adjust(1)

if __name__ == '__main__':
    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')
    dp.run_polling(bot)
