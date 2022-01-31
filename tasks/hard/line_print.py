"""
Написать рекурсивную функцию  line_print, которая принимает 1 аргумент - список

Функция печатает каждых элемент на новой строке.

Если элемент списка - список, то его элементы должны выводиться с отступом
относительно родительского на 4 пробела

Например:

some_list = [1, 2, [1, 2, [5, 7], 3], 8]

line_print(some_list)
1
2
    1
    2
        5
        7
    3
8
"""


def line_print(collections: list | int, indent: int = 0):
    for item in collections:
        if isinstance(item, list):
            line_print(item, indent + 1)
        else:
            print(' ' * 4 * indent + str(item))
