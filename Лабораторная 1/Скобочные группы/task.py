def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    br_list: list = []
    br_list.extend(brackets_row)
    if len(br_list) == 0:
        return True
    if len(br_list) % 2 == 0:
        if br_list.count('(') == br_list.count(')') and br_list[0] == '(' and br_list[-1] == ')':
            return True
    return False

if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(""))  # True
    print(check_brackets(")("))  # False
