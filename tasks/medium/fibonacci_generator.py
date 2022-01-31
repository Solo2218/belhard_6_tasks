"""
Написать генератор fibonacci, которая принимает номер значения num_count
из чисел Фибоначчи и выводит на экран результат до заданного значения.

Номер значения нужно проверить

Пример:

fibonacci(0) -> raise ValueError('Введите значение больше 1')
fibonacci(5)
1
2
3
5
8
Traceback (most recent call last):
File «C:/Python/Python3/python_generator.py», line 29, in
print(next(fib))
StopIteration
"""


def fibonacci(num_count: int) -> int:
    fib1 = 0
    fib2 = 1
    if num_count >= 1:
        for _ in range(num_count):
            yield fib2
            fib1, fib2 = fib2, fib1 + fib2
    else:
        raise ValueError('Введите значение больше 1')
