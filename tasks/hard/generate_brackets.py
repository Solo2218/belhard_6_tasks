"""
Задача из собеседования в яндекс

Написать рекурсивную функцию generate_brackets, которая принимает длину -
количество пар скобок, и будет генерировать все возможные варианты
скобочных последовательностей


Например:
generate_brackets(3)
n = 3
((()))
(()())
(())()
()(())
()()()

n = 4
(((())))
((()()))
((())())
((()))()
(()(()))
(()()())
(()())()
(())(())
(())()()
()((()))
()(()())
()(())()
()()(())
()()()()
"""


def generate_brackets(n: int, result: str = '', begin: int = 0, close: int = 0) -> None:
    if len(result) == (n * 2):
        print(result)
    if begin < n:
        generate_brackets(n, result + '(', begin + 1, close)
    if close < begin:
        generate_brackets(n, result + ')', begin, close + 1)
