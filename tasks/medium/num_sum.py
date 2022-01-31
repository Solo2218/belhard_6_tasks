"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""


def sum_of_numbers(number: int):
    if number < 10:
        return number
    else:
        return number % 10 + sum_of_numbers(number // 10)