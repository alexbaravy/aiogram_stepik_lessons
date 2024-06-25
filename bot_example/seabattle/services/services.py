import copy
from aiogram.filters.callback_data import CallbackData

from user_data import users
from services.ships_generator import field, FIELD_SIZE

ships = field

# Создаем свой класс фабрики коллбэков, указывая префикс
# и структуру callback_data
class FieldCallbackFactory(CallbackData, prefix="user_field"):
    x: int
    y: int


# Функция, которая пересоздает новое поле для каждого игрока
def reset_field(user_id: int) -> None:
    users[user_id]['ships'] = copy.deepcopy(ships)
    users[user_id]['field'] = [
        [0 for _ in range(FIELD_SIZE)]
        for _ in range(FIELD_SIZE)
    ]
