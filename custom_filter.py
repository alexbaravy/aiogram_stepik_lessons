import os
from environs import Env

import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.types import Message

env = Env()  # Создаем экземпляр класса Env
env.read_env()  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
bot_token = env('BOT_TOKEN')  # Получаем и сохраняем значение переменной окружения в переменную bot_token

'''
Реализуйте функцию custom_filter(), которая на вход принимает строку some_str,
находит в ней целые числа, отбирает из них те, что делятся нацело на 7, суммирует их, а затем проверяет:
превышает эта сумма 83 или нет.

Если НЕ превышает - функция должна вернуть True, если превышает - False.
'''

# Создаем объекты бота и диспетчера
bot = Bot(token=bot_token)
dp = Dispatcher()


@dp.message()
async def custom_filter(message: Message):
    # Разбиваем текст на слова
    words = message.text.split()

    # Инициализируем сумму
    total_sum = 0

    # Проходим по каждому слову в тексте
    for word in words:
        # Пытаемся преобразовать слово в целое число
        try:
            num = int(word)
            # Проверяем условие: число делится нацело на 7
            if num % 7 == 0:
                # Если число подходит, добавляем его к сумме
                total_sum += num
        except ValueError:
            # Пропускаем слова, которые невозможно преобразовать в число
            pass

    # Проверяем условие: сумма чисел превышает 83
    if total_sum > 83:
        await message.answer(f'False: Сумма чисел, делящихся на 7 из вашего сообщения, превышает 83: {total_sum}')
    else:
        await message.answer(f'True: Сумма чисел, делящихся на 7 из вашего сообщения, не превышает 83: {total_sum}')



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    dp.run_polling(bot)