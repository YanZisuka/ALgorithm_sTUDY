from heapq import *
import sys
input = sys.stdin.readline


def dijkstra(s):
    dist = [float('inf')] * (n+1)
    dist[s] = 0
    heap = []
    heappush(heap, (0, s))

    while heap:
        dt, now = heappop(heap)

        if dist[now] < dt:
            continue

        for next, weight in graph[now]:
            shtst = dist[now] + weight
            if shtst < dist[next]:
                dist[next] = shtst
                heappush(heap, (shtst, next))
    return dist


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())
dist = dijkstra(start)

print(dist[end])