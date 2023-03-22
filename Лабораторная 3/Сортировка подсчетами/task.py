from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    ...  # TODO реализовать алгоритм сортировки подсчетами
    temp: dict = {}
    ans: list = []
    for elem in container:
        if elem in temp:
            temp[elem] += 1
        else:
            temp[elem] = 1
    for key, value in sorted(temp.items(), key= lambda x: x[0]):
        ans.extend([key]*value)
    return ans
        
       
        
        
