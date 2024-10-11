'''7.4 Фильтры Реализуйте функцию custom_filter(), которая:
 1. на вход принимает список some_list, с любыми типами данных
 2. находит в этом списке целые числа
 3. отбирает из них те, что делятся нацело на 7
 4  суммирует их
 5. проверяет: превышает эта сумма 83 или нет.
 Если НЕ превышает - функция должна вернуть True, если превышает - False.'''

from environs import Env

import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

# Load environment variables
env = Env()
env.read_env()
bot_token = env('BOT_TOKEN')

# Create bot and dispatcher instances
bot = Bot(token=bot_token)
dp = Dispatcher()


def sum_divisible_by_seven(numbers):
    """Sum integers from the list that are divisible by 7."""
    total_sum = sum(num for num in numbers if isinstance(num, int) and num % 7 == 0)
    return total_sum


@dp.message(Command(commands="start"))
async def process_start_command(message: Message):
    await message.answer("Привет. Введи строку состоящую из цифр и букв.\nПример: 12 5 7 h a s 14 24")


@dp.message()
async def custom_filter(message: Message):
    # Split the text into words and attempt to convert to integers
    words = message.text.split()
    numbers = []

    for word in words:
        try:
            num = int(word)
            numbers.append(num)
        except ValueError:
            continue  # Skip non-integer words

    # Calculate the total sum of numbers divisible by 7
    total_sum = sum_divisible_by_seven(numbers)

    # Check if the total sum exceeds 83 and respond accordingly
    if total_sum > 83:
        await message.answer(f'False: Сумма чисел, делящихся на 7 из вашего сообщения, превышает 83: {total_sum}')
    else:
        await message.answer(f'True: Сумма чисел, делящихся на 7 из вашего сообщения, не превышает 83: {total_sum}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    dp.run_polling(bot)
