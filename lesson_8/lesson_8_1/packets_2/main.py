"""8.1 Модули и пакеты
Относительные импорты
https://stepik.org/lesson/759401/step/5?unit=761417
"""

print('Basic module main.py.\nIts name during program execution', __name__)
print('=========================')

from pack_1.file_11 import result
from pack_2.pack_21.file_211 import r

print('result =', result)
print('r =', r)


