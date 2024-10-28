"""8.1 Модули и пакеты
Модули
https://stepik.org/lesson/759401/step/2?unit=761417
"""
print(dir())

import functions
from data import my_dict
from classes import *

print('This is exec file')

if __name__=='__main__':
    print('=========================')
    print('The code below will not execute if this file is an imported module into another executable')
    print('=========================')
    print(functions.get_double_number(25))
    print('=========================')
    print(my_dict)
    print('=========================')
    MyClass()
    print('=========================')
    print(dir())
    print('=========================')
    print(dir(functions))


import sys

print(sys.path)