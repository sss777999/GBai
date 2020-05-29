'''
2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
которые необходимо обойти.
'''
g = [[0, 0, 1, 1, 9, 0, 0, 0],
     [0, 0, 9, 4, 0, 0, 5, 0],
     [0, 9, 0, 0, 3, 0, 6, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 5, 0],
     [0, 0, 7, 0, 8, 1, 0, 0],
     [0, 0, 0, 0, 0, 1, 2, 0]]


def dijkstra(graph, start):
    begin = start
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [[] for i in range(length)]

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = []
                    if len(parent[start]) > 0:
                        for j in parent[start]:
                            parent[i].append(j)
                    parent[i].append(start)

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    for i in range(len(parent)):
        if len(parent[i]) > 0:
            parent[i].append(i)
        else:
            parent[i] = ['нет пути!']
    parent[begin] = begin
    for i in range(length):
        print(f'{i} минимальная стоимость: {cost[i]}; самый быстрый путь: {parent[i]}')
    return cost


s = int(input('Введите вершину с которой начать: '))
print(dijkstra(g, s))
