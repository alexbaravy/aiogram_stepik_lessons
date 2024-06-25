import numpy as np
import random

# Размеры матрицы
FIELD_SIZE = 8

# Инициализация пустого поля
field = np.zeros((FIELD_SIZE, FIELD_SIZE), dtype=int)

# Определение размеров кораблей
ships = {
    4: 1,  # Один четырёхпалубный
    3: 2,  # Два трёхпалубных
    2: 3,  # Три двухпалубных
    1: 4   # Четыре однопалубных
}

def check_space(field, x, y, length, orientation):
    """Проверка наличия места для корабля и отсутствия соприкосновений"""
    if orientation == 'horizontal':
        if y + length > FIELD_SIZE:
            return False
        for i in range(x-1, x+2):
            for j in range(y-1, y+length+1):
                if i >= 0 and i < FIELD_SIZE and j >= 0 and j < FIELD_SIZE:
                    if field[i, j] != 0:
                        return False
    elif orientation == 'vertical':
        if x + length > FIELD_SIZE:
            return False
        for i in range(x-1, x+length+1):
            for j in range(y-1, y+2):
                if i >= 0 and i < FIELD_SIZE and j >= 0 and j < FIELD_SIZE:
                    if field[i, j] != 0:
                        return False
    return True

def place_ship(field, length):
    """Размещение одного корабля на поле"""
    placed = False
    while not placed:
        orientation = random.choice(['horizontal', 'vertical'])
        x = random.randint(0, FIELD_SIZE-1)
        y = random.randint(0, FIELD_SIZE-1)
        if check_space(field, x, y, length, orientation):
            if orientation == 'horizontal':
                field[x, y:y+length] = 1
            elif orientation == 'vertical':
                field[x:x+length, y] = 1
            placed = True

# Размещение всех кораблей
for length, count in ships.items():
    for _ in range(count):
        place_ship(field, length)

print(field)