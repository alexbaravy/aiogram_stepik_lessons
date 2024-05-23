from environs import Env
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.filters.callback_data import CallbackData
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


# Создаем свой класс фабрики коллбэков, указывая префикс
class GoodsCallbackFactory(CallbackData, prefix='goods', sep='|'):
    category_id: int
    subcategory_id: int
    item_id: int


# Создаем объекты кнопок, с применением фабрики коллбэков
button_1 = InlineKeyboardButton(
    text='Category 1',
    callback_data=GoodsCallbackFactory(
        category_id=1,
        subcategory_id=0,
        item_id=0
    ).pack()
)

button_2 = InlineKeyboardButton(
    text='Category 2',
    callback_data=GoodsCallbackFactory(
        category_id=2,
        subcategory_id=0,
        item_id=0
    ).pack()
)

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[button_1], [button_2]]
)


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру с инлайн-кнопками
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Вот такая клавиатура',
        reply_markup=keyboard
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


if __name__ == '__main__':
    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')
    dp.run_polling(bot)
