"""8.1 Модули и пакеты
Некоторые нюансы импортов в __init__.py
https://stepik.org/lesson/759401/step/7?unit=761417"""

print('This is main.py: __main__')
print('=========================')

import pack_1
import pack_2
from pack_2 import pack_21

print(dir())
print(dir(pack_1))
print(dir(pack_2))
print(dir(pack_21))

print(pack_21.some_func('some_text', 2))
