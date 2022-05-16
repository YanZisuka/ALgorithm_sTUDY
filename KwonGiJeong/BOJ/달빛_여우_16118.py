import sys
from heapq import heappush, heappop

input = sys.stdin.readline

def dijkstra_Fox(s):
    queue = []
    distance = [INF] * (N + 1)
    distance[s] = 0
    heappush(queue, (0, s))

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
    distance = [[INF] * (N + 1) for _ in range(2)]
    distance[1][s] = 0
    heappush(queue, (0, s, True))

    while queue:
        temp_weight, temp_node, is_odd = heappop(queue)

        if (is_odd == True) and (distance[0][temp_node] < temp_weight):
            continue
        if (is_odd == False) and (distance[1][temp_node] < temp_weight):
            continue

        for next_node, weight in graph[temp_node]:
            if is_odd:
                next_weight = temp_weight + (weight * 2)
                if next_weight < distance[0][next_node]:
                    distance[0][next_node] = next_weight
                    heappush(queue, (next_weight, next_node, False))

            else:
                next_weight = temp_weight + (weight / 2)
                if next_weight < distance[1][next_node]:
                    distance[1][next_node] = next_weight
                    heappush(queue, (next_weight, next_node, True))

    return distance

INF = sys.maxsize
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

fox_distance = dijkstra_Fox(1)
wolf_distance = dijkstra_Wolf(1)

cnt = 0

for i in range(1, N + 1):
    if fox_distance[i] < min(wolf_distance[0][i], wolf_distance[1][i]):
        cnt += 1

print(cnt)