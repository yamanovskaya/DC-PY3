"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    arr_len = len(arr)
    if arr_len == 0:
        raise ValueError
    elif arr_len == 1:
        return 0
    else:
        elem_temp = arr[0]
        ind_temp = 0
        for i in range(arr_len - 1):
            if arr[i + 1] < elem_temp:
                elem_temp = arr[i + 1]
                ind_temp = i + 1
        return ind_temp
