import sys
from heapq import heappush, heappop

input = sys.stdin.readline

def dijkstra(s):
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
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())

one = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

answer = min(one[v1] + v1_distance[v2] + v2_distance[N], one[v2] + v2_distance[v1] + v1_distance[N])

if answer < INF:
    print(answer)
else:
    print(-1)