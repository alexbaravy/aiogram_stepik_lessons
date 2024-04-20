from environs import Env
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           KeyboardButtonPollType)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types.web_app_info import WebAppInfo

env = Env()  # Создаем экземпляр класса Env
env.read_env()  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
bot_token = env('BOT_TOKEN')  # Получаем и сохраняем значение переменной окружения в переменную bot_token

bot = Bot(token=bot_token)
dp = Dispatcher()

# Инициализируем билдер
kb_builder = ReplyKeyboardBuilder()

# Создаем кнопки
btn_1 = KeyboardButton(text='Кнопка 1')
btn_2 = KeyboardButton(text='Кнопка 2')

# Добавляем кнопки в билдер
kb_builder.row(btn_1, btn_2, width=1)

# Создаем объект клавиатуры
keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Нажмите на кнопку ниже'
)


# Этот хэндлер будет срабатывать на команду "/placeholder"
@dp.message(CommandStart())
async def process_placeholder_command(message: Message):
    await message.answer(
        text='Экспериментируем с полем placeholder',
        reply_markup=keyboard
    )


@dp.message(lambda message: message.text in ["Кнопка 1", "Кнопка 2"])
async def process_placeholder_command(message: Message):
    await message.answer(
        text='Молодец, нажал нужную кнопку',
        reply_markup=keyboard
    )


@dp.message()
async def process_other_messages(message: Message):
    await message.answer(
        text='Пожалуйста, нажмите кнопку "Кнопка 1" или "Кнопка 2".',
        reply_markup=keyboard
    )


if __name__ == '__main__':
    dp.run_polling(bot)
