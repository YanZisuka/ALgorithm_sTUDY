import sys
from heapq import heappush, heappop

input = sys.stdin.readline

def dijkstra(s):
    global queue
    global distance

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
                heappush(queue, [next_weight, next_node])


INF = sys.maxsize
V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)
queue = []

for _ in range(E):
    u, v, w = map(int, input.split())
    graph[u].append([v, w])

dijkstra(start)

for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])