"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и
False, если нет

Нельзя пользоваться операцией возведения в степень
"""


def check_number(number: int) -> bool:
    if number == 1:
        return True
    elif number < 2:
        return False
    return (check_number(number / 2))