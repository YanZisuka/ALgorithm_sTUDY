from heapq import *
import sys
input = sys.stdin.readline


def foxDijkstra(s):
    dist = [float('inf')] * (n+1)
    dist[s] = 0
    heap = []
    heappush(heap, (0, s))

    while heap:
        dt, now = heappop(heap)

        if dist[now] < dt:
            continue

        for next, weight in graph[now]:
            shortest = dist[now] + weight
            if shortest < dist[next]:
                dist[next] = shortest
                heappush(heap, (shortest, next))
    return dist


def wolfDijkstra(s):
    dist = [[float('inf')] * (n+1) for _ in range(2)]  # 0: 해당 노드에 달려서 도달, 1: 해당 노드에 걸어서 도달
    dist[1][s] = 0
    heap = []
    heappush(heap, (0, s, False))

    while heap:
        dt, now, slow = heappop(heap)

        if slow and dist[0][now] < dt:
            continue
        if not slow and dist[1][now] < dt:
            continue
        
        for next, weight in graph[now]:
            if slow:
                shortest = dt + weight * 2
                if shortest < dist[1][next]:
                    dist[1][next] = shortest
                    heappush(heap, (shortest, next, False))
            if not slow:
                shortest = dt + weight / 2
                if shortest < dist[0][next]:
                    dist[0][next] = shortest
                    heappush(heap, (shortest, next, True))
    return dist


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
ans = 0

for i in range(m):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

fox = foxDijkstra(1)
wolf = wolfDijkstra(1)

for i in range(1, n+1):
    if fox[i] < min(wolf[0][i], wolf[1][i]):
        ans += 1

print(ans)