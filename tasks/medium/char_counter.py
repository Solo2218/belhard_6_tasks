"""
Написать функцию count_char, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}

Нельзя пользоваться collections.Counter!
"""
STR_VAL = 'python is the fastest-growing major programming language'


def count_char(STR_VAL: str) -> dict:
    list_str_val = list(STR_VAL)
    dict_str_val = {}
    for i in range(len(list_str_val)):
        symbol = list_str_val[i]
        if symbol not in dict_str_val.keys():
            dict_str_val[symbol] = 1
        else:
            dict_str_val[symbol] += 1
    return dict_str_val
