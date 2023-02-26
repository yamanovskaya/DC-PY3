"""
My little Queue
"""
from typing import Any
import doctest


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        Начало очереди это элемент списка с индексом 0 (появившийся в очереди раньше всего)
        Конец очереди это элемент списка с индексом -1 (появившийся в очереди позже всего)
            >>> queue_ = Queue()
            >>> print(queue_.list_ == [] and isinstance(queue_.list_, list))
            True
        """
        self.list_: list = []

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
            >>> queue_ = Queue()
            >>> queue_.enqueue('element 1')
            >>> queue_.enqueue('element 2')
            >>> queue_.enqueue('element 3')
            >>> print(queue_.list_ == ['element 1', 'element 2', 'element 3'])
            True
        """
        self.list_.append(elem)

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.

            >>> queue_ = Queue()
            >>> queue_.enqueue('element 1')
            >>> queue_.enqueue('element 2')
            >>> queue_.enqueue('element 3')
            >>> print(queue_.dequeue() == 'element 1', queue_.list_)
            True ['element 2', 'element 3']
            >>> queue_ = Queue()
            >>> a = queue_.dequeue()
            Queue is empty
        """

        if len(self.list_) == 0:
            raise IndexError('Queue is empty')
        return self.list_.pop(0)

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента

            >>> queue_ = Queue()
            >>> queue_.enqueue('element 1')
            >>> queue_.enqueue('element 2')
            >>> queue_.enqueue('element 3')
            >>> print(queue_.peek(), queue_.list_)
            element 1 ['element 1', 'element 2', 'element 3']
        """
        if not isinstance(ind, int):
            raise TypeError('index must be int')
        if not abs(ind) < len(self) - 1:
            raise IndexError('index is out of range')
        return self.list_[ind]

    def clear(self) -> None:
        """ Очистка очереди.
            >>> queue_ = Queue()
            >>> queue_.enqueue('element 1')
            >>> queue_.enqueue('element 2')
            >>> queue_.enqueue('element 3')
            >>> queue_.clear()
            >>> print(queue_.list_)
            []
        """
        # del self.list_
        self.list_.clear()

    def __len__(self):
        """ Количество элементов в очереди.
            >>> queue_ = Queue()
            >>> queue_.enqueue('element 1')
            >>> queue_.enqueue('element 2')
            >>> queue_.enqueue('element 3')
            >>> print(len(queue_.list_))
            3
            """
        return len(self.list_)


# doctest.testmod()  # тестирование примеров