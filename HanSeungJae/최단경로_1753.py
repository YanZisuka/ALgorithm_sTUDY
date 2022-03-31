from heapq import *
import sys
input = sys.stdin.readline


def dijkstra(start):
    dist[start] = 0
    heappush(heap, (0, start))

    while heap:
        distance, now = heappop(heap)

        if dist[now] < distance:
            continue
        
        for next, weight in graph[now]:
            shortest = distance + weight
            if shortest < dist[next]:
                dist[next] = shortest
                heappush(heap, (shortest, next))
        
 
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
heap = []
dist = [float('INF')] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(K)

for i in range(1, V+1):
    if dist[i] != float('inf'):
        print(dist[i])
    else:
        print('INF')
