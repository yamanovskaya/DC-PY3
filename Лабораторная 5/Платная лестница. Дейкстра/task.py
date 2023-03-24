from typing import Union

import networkx as nx


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """

    _, dict_dist = nx.dijkstra_predecessor_and_distance(graph, 0)
    a = len(dict_dist) - 1
    return dict_dist[a]


def generate_graph(tup):
    l = len(tup)
    ans: list = []
    for i in range(l):
        if (i + 1) < l:
            ans.append((i, i + 1, tup[i]))
            if (i + 2) < l:
                ans.append((i, i + 2, tup[i + 1]))
    graph = nx.DiGraph()
    graph.add_weighted_edges_from(ans)
    return graph


if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = generate_graph(stairway)
    print(stairway_path(stairway_graph))  # 72
