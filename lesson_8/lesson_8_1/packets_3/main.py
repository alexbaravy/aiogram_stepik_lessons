"""8.1 Модули и пакеты
__init__.py - инициализатор пакета
https://stepik.org/lesson/759401/step/6?unit=761417"""


print('Basic module main.py')
print('Its name during program execution', __name__)
print('=========================')

import pack_2


print(dir())
print(dir(pack_2))

print(pack_2.another_some_func(25))



