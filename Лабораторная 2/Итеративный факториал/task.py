def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError
    temp = 1
    for i in range(n):
        temp *= i + 1
    return temp
