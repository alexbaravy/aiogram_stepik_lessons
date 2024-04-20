from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU

# Инициализируем роутер уровня модуля
router: Router = Router()

@router.message()
async def send_something(message: Message):
    await message.reply(text=LEXICON_RU['something'])
