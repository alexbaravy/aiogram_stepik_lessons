"""8.1 Модули и пакеты
Пакеты
https://stepik.org/lesson/759401/step/4?unit=761417
"""

print('Basic module main.py.\nIts name during program execution', __name__)
print('=========================')

from pack_1.file_11 import a
from pack_2.pack_21 import file_211
from pack_2.pack_21.file_211 import b

print('a =', a)
print('b =', b)
print('some_dict:', file_211.some_dict)
