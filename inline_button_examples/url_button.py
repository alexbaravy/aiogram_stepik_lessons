from environs import Env

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message



env = Env()  # Создаем экземпляр класса Env
env.read_env()  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
bot_token = env('BOT_TOKEN')  # Получаем и сохраняем значение переменной окружения в переменную bot_token
user_id = env('USER_ID')

# Создаем объекты бота и диспетчера
bot = Bot(token=bot_token)
dp = Dispatcher()

# Создаем объекты инлайн-кнопок
url_button_1 = InlineKeyboardButton(
    text='Курс "Телеграм-боты на Python и AIOgram"',
    url='https://stepik.org/120924'
)
url_button_2 = InlineKeyboardButton(
    text='Документация Telegram Bot API',
    url='https://core.telegram.org/bots/api'
)

url_button_3 = InlineKeyboardButton(
    text='Группа "Телеграм-боты на AIOgram"',
    url=f'tg://resolve?domain=aiogram_stepik_course'
)

url_button_4 = InlineKeyboardButton(
    text='Кнопка на мой профиль',
    url=f'tg://user?id={user_id}'
)

channel_name = 'toBeAnMLspecialist'
url_button_5 = InlineKeyboardButton(
    text='Канал "Стать специалистом по машинному обучению"',
    url=f'https://t.me/aiogram_stepik_course'
)

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[url_button_1],
                     [url_button_2],
                     [url_button_3],
                     [url_button_4],
                     [url_button_5]]
)


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру c url-кнопками
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Это инлайн-кнопки с параметром "url"',
        reply_markup=keyboard
    )


if __name__ == '__main__':
    dp.run_polling(bot)