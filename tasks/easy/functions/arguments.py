"""
Написать функцию dict_from_args, которая принимает неограниченное
количество позиционных аргументов и неограниченное количество аргументов
ключевых-слов.

Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
нет, то кинуть ошибку TypeError("Все позиционные аргументы должны быть целыми").
Проверить, что все аргументы целые можно с помощью функции all:
https://pyneng.readthedocs.io/ru/latest/book/10_useful_functions/all_any.html

Если все аргументы - ключевые слова являются строками, то найти максимальную
длину слова. Если нет, то кинуть ошибку TypeError("Все аргументы - ключевые
слова должны быть строками").

Функция должна вернуть словарь, вида:
{
    "args_sum": 13,
    "kwargs_max_len": 7
}
"""


def dict_from_args(*args, **kwargs):
    result = {}
    if all(type(x) is int for x in args):
        result['args_sum'] = sum(args)
    else:
        raise TypeError('Все позиционные аргументы должны быть целыми')
    value = list(kwargs.values())
    if all(type(x) is str for x in value):
        length = len(value[0])
        for i in range(len(value) - 1):
            if length < len(value[i + 1]):
                length = len(value[i + 1])
        result['kwargs_max_len'] = length
    else:
        raise TypeError('Все аргументы - ключевые слова должны быть строками')
    return result
