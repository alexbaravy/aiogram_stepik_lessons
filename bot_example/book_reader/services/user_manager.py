import logging
from copy import deepcopy
from typing import Union
from database.database import user_dict_template

# Инициализируем логгер
logger = logging.getLogger(__name__)


class UserManager:
    def __init__(self):
        self.users = {}

    # Проверка на существования пользователя
    def ensure_user_exists(self, user_id: int):
        if user_id not in self.users:
            self.users[user_id] = deepcopy(user_dict_template)
        logger.info(self.users[user_id])

    # Получение текущей страницы пользователя
    def get_user_page(self, user_id: int):
        self.ensure_user_exists(user_id)
        logger.info(self.users[user_id])
        return self.users[user_id]['current_page']

    # Изменение номера страницы
    def change_user_page(self, user_id: int, change: Union[-1, 1]):
        self.users[user_id]['current_page'] += change
        logger.info(self.users[user_id])
        return self.users[user_id]['current_page']

    # Сброс нумерации страниц
    def reset_user_page(self, user_id: int):
        self.ensure_user_exists(user_id)
        self.users[user_id]['current_page'] = 1
        logger.info(self.users[user_id])
        return self.users[user_id]['current_page']

    # Получение закладок
    def get_user_bookmarks(self, user_id):
        self.ensure_user_exists(user_id)
        logger.info(self.users[user_id])
        return self.users[user_id]['bookmarks']

    # Перейти на закладку
    def go_bookmark(self, user_id, page):
        self.ensure_user_exists(user_id)
        self.users[user_id]['current_page'] = page
        logger.info(self.users[user_id])
        return self.users[user_id]['current_page']
