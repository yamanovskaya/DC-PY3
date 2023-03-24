from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    ...  # TODO решить задачу с помощью динамического программирования
    if n <= 0 or m <= 0:
        raise ValueError
    table: list = [[0]*(m+2) for _ in range(n+2)]
    table[1][1] = 1
    for row in range(1, n+1):
        for col in range(1, m+1):
            table[row][col] += table[row-1][col] + table[row][col-1] + table[row-1][col-1]
    return [row[1:m+1] for row in table[1:n+1]]


if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
