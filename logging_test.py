import logging
import sys


# Определяем свой фильтр, наследуюясь от класса Filter библиотеки logging
class ErrorLogFilter(logging.Filter):
    # Переопределяем метод filter, который принимает `self` и `record`
    # Переменная рекорд будет ссылаться на объект класса LogRecord
    def filter(self, record):
        # атрибуты и значения у record
        # if record.levelname == 'ERROR' and 'важно' in record.msg.lower():
        #     for attr in dir(record):
        #         value = getattr(record, attr)
        #         print(f'{attr} -> {value}')
        return record.levelname == 'ERROR' and 'важно' in record.msg.lower()


# Определяем форматы для логов
format_1 = '#%(levelname)-8s [%(asctime)s] - %(filename)s:' \
           '%(lineno)d - %(name)s - %(message)s'
format_2 = '[{asctime}] #{levelname:8} {filename}:' \
           '{lineno} - {name} - {message}'

# Инициализируем форматтеры
formatter_1 = logging.Formatter(fmt=format_1)
formatter_2 = logging.Formatter(fmt=format_2, style='{')

# Создаем логгер
logger = logging.getLogger(__name__)

# Инициализируем хэндлеры для вывода логов в stderr и stdout
stderr_handler = logging.StreamHandler()
stdout_handler = logging.StreamHandler(sys.stdout)

# Инициализируем хэндлер для записи логов в файл
file_handler = logging.FileHandler('logs.log')

# Подключаем фильтр к хэндлеру
file_handler.addFilter(ErrorLogFilter())


# Устанавливаем уровень логов на уровне логгера
logger.setLevel(logging.DEBUG)
# либо
# Устанавливаем уровни логов на уровне хэндлеров
stderr_handler.setLevel(logging.INFO)
stdout_handler.setLevel(logging.DEBUG)

# Устанавливаем форматтеры для хэндлеров
stderr_handler.setFormatter(formatter_1)
stdout_handler.setFormatter(formatter_2)
file_handler.setFormatter(formatter_2)

# Добавляем хэндлеры логгеру
logger.addHandler(stderr_handler)
logger.addHandler(stdout_handler)
logger.addHandler(file_handler)

# Создаем, выводим и записываем логи
logger.debug('Это лог для отладки!')
logger.info('Это лог с информацией!')
logger.warning('Это лог с предупреждением!')
logger.error('Важно! Это лог с ошибкой!')
logger.critical('Это лог с критической ошибкой!')

# logging.debug('Это лог уровня DEBUG')
# logging.info('Это лог уровня INFO')
# logging.warning('Это лог уровня WARNING')
# logging.error('Это лог уровня ERROR')
# logging.critical('Это лог уровня CRITICAL')