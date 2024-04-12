import logging

logger = logging.getLogger(__name__)

try:
    print(4 / 2)
    print(2 / 0)
except ZeroDivisionError:
    logger.error('Тут было исключение', exc_info=True)
    # logger.exception('Тут было исключение')


# import sys
# import logging
#
# # Настройка логгирования
# logging.basicConfig(format='#%(levelname)-8s [%(asctime)s] - %(filename)s:' \
#            '%(lineno)d - %(name)s - %(message)s', filename='errors.log', level=logging.ERROR)
#
# # Перехватываем стандартный поток ошибок
# def excepthook(exc_type, exc_value, traceback):
#     logging.error("Тут было исключение:", exc_info=(exc_type, exc_value, traceback))
#
# sys.excepthook = excepthook
#
# # Выполнение кода, где может произойти ошибка
# print(4 / 2)
# print(1 / 0)