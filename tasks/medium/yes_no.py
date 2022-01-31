"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(some_list: list):
    for i in range(len(some_list)):
        result = "No"
        for n in range(i):
            if some_list[i] == some_list[n]:
                result = "Yes"
                break
        print(result)