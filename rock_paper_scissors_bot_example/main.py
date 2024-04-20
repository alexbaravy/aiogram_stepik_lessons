import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties

from config_data.config import Config, load_config
from handlers import user_handlers, game_handlers, other_handlers
from lexicon.lexicon_ru import LEXICON_RU

# Инициализируем логгер
logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота
async def main() -> None:
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML)

              )
    dp = Dispatcher()

    # Создаем асинхронную функцию
    async def set_main_menu(bot: Bot):
        # Создаем список с командами и их описанием для кнопки menu
        main_menu_commands = [
            BotCommand(command='/start',
                       description=LEXICON_RU['start_button']),
            BotCommand(command='/help',
                       description=LEXICON_RU['help_button']),
            BotCommand(command='/stat',
                       description=LEXICON_RU['stat_button']),
            BotCommand(command='/exit',
                       description=LEXICON_RU['exit_button']),
        ]

        await bot.set_my_commands(main_menu_commands)

    # Регистрируем асинхронную функцию в диспетчере,
    # которая будет выполняться на старте бота,
    dp.startup.register(set_main_menu)

    # Регистриуем роутеры в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(game_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    atexit.register(save_users)


asyncio.run(main())
