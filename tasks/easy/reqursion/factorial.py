"""
Написать рекурсивную функцию factorial, которая будет возвращать n-ый элемент

5! = 1 * 2 * 3 * 4 * 5 = 125
"""


def factorial(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
