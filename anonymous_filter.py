"""Напишите функцию anonymous_filter, используя синтаксис анонимных функций, которая принимает строковый аргумент и
возвращает значение True, если количество русских букв я не меньше 23 (регистр буквы неважен) и False в противном
случае."""

import re

anonymous_filter_1 = lambda s: len(re.findall('[я]', s.lower())) >= 23
anonymous_filter_2 = lambda s: sum(1 for char in s.lower() if char == 'я') >= 23

print(anonymous_filter_1('Я - последняя буква в алфавите!'))
print(anonymous_filter_1('яяяяяяяяяяяяяяяяяяяяяяяя, яяяяяяяяяяяяяяяя и яяяяяяяя тоже!'))

print(anonymous_filter_2('Я - последняя буква в алфавите!'))
print(anonymous_filter_2('яяяяяяяяяяяяяяяяяяяяяяяя, яяяяяяяяяяяяяяяя и яяяяяяяя тоже!'))