import sys
from heapq import *
input = sys.stdin.readline


def dijkstra(s):
    dist = [(float('inf'), [])] * (n+1)
    dist[s] = (0, [s])
    heap = []
    heappush(heap, (dist[s], s))

    while heap:
        (dst, path), now = heappop(heap)

        if dist[now][0] < dst:
            continue

        for nxt, weight in graph[now]:
            shortest = dist[now][0] + weight
            if shortest < dist[nxt][0]:
                dist[nxt] = (shortest, path+[nxt])
                heappush(heap, (dist[nxt], nxt))
    return dist


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, goal = map(int, input().split())

dist = dijkstra(start)

print(dist[goal][0], len(dist[goal][1]), ' '.join(map(str, dist[goal][1])), sep='\n')