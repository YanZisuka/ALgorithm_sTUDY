from heapq import *
import sys
input = sys.stdin.readline


def dijkstra(s):
    dist = [float('inf')] * (n+1)
    dist[s] = 0
    heap = []
    heappush(heap, (0, s))

    while heap:
        dt, v = heappop(heap)

        if dist[v] < dt:
            continue

        for next, weight in graph[v]:
            shtst = dt + weight
            if shtst < dist[next]:
                dist[next] = shtst
                heappush(heap, (shtst, next))
    return dist


n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

distOf1 = dijkstra(1)
distOfv1 = dijkstra(v1)
distOfv2 = dijkstra(v2)

case1 = distOf1[v1] + distOfv1[v2] + distOfv2[n]
case2 = distOf1[v2] + distOfv2[v1] + distOfv1[n]

ans = min(case1, case2)

if ans < float('inf'):
    print(ans)
else:
    print(-1)