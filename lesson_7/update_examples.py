# 7.2 Апдейт (Update)

from environs import Env
from pprint import pprint


from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


env = Env()  # Создаем экземпляр класса Env
env.read_env()  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
bot_token = env('BOT_TOKEN')  # Получаем и сохраняем значение переменной окружения в переменную bot_token

# Создаем объекты бота и диспетчера
bot = Bot(token=bot_token)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    try:
        pprint(vars(message))
        print(message.model_dump_json(indent=4, exclude_none=True))
        await message.send_copy(chat_id=message.chat.id)
    except TypeError as e:
        await message.reply(
            f'Данный тип апдейтов не поддерживается методом send_copy: {e}'
        )


if __name__ == '__main__':
    dp.run_polling(bot)
