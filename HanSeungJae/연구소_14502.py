from collections import deque
from itertools import combinations
import copy


def set_empty(graph):
    empty = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                empty.append((i, j))
    return empty


def set_virus(graph):
    virus = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                virus.append((i, j))
    return virus


def BruteForce(empty, graph):
    graphs = []
    for com in combinations(empty, 3):
        tmp_graph = copy.deepcopy(graph)
        for i, j in com:
            tmp_graph[i][j] = 1
        graphs.append(tmp_graph)
    return graphs


def BFS(graph, a, b):
    queue = deque()
    queue.append((a, b))
    cnt = 0

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m:
                if graph[ni][nj] == 0:
                    graph[ni][nj] = 2
                    queue.append((ni, nj))
    for i in range(n):
        cnt += graph[i].count(0)
    return cnt


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

empty = set_empty(graph)
virus = set_virus(graph)
graphs = BruteForce(empty, graph)
safety_zones = []
for graph in graphs:
    temp = []
    for i, j in virus:
        temp.append(BFS(graph, i, j))
    safety_zones.append(min(temp))

print(max(safety_zones))