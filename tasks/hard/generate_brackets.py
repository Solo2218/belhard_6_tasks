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


def generate_brackets(n: int, result: str = '', open: int = 0, close: int = 0) -> None:
    if len(result) == (n * 2):
        print(result)
    if open < n:
        generate_brackets(n, result + '(', open + 1, close)
    if close < open:
        generate_brackets(n, result + ')', open, close + 1)