import sys
from heapq import heappush, heappop

input = sys.stdin.readline

def dijkstra_Fox(s):
    queue = []
    distance = [INF] * (N + 1)
    distance[1] = 0
    heappush(queue, [0, 1])

    while queue:
        temp_weight, temp_node = heappop(queue)

        if distance[temp_node] < temp_weight:
            continue

        for next_node, weight in graph[temp_node]:
            next_weight = temp_weight + weight

            if next_weight < distance[next_node]:
                distance[next_node] = next_weight
                heappush(queue, (next_weight, next_node))

    return distance

def dijkstra_Wolf(s):
    queue = []
    distance = [INF] * (N + 1)
    distance[s] = 0
    heappush(queue, [0, s])

    while queue:
        temp_weight, temp_node = heappop(queue)

        if distance[temp_node] < temp_weight:
            continue

        for next_node, weight in graph[temp_node]:
            next_weight = temp_weight + weight

            if next_weight < distance[next_node]:
                distance[next_node] = next_weight
                heappush(queue, (next_weight, next_node))

    return distance

INF = sys.maxsize
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, d = map(int, input().split())
    graph[a].append((d * 2, b))
    graph[b].append((d * 2, a))


answer = min(one[v1] + v1_distance[v2] + v2_distance[N], one[v2] + v2_distance[v1] + v1_distance[N])

if answer < INF:
    print(answer)
else:
    print(-1)