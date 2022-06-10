import sys
from heapq import *
input = sys.stdin.readline


INF = float('inf')

def dijkstra(s):
    dist = [INF] * (100001)
    pq = []
    dist[s] = 0
    heappush(pq, (dist[s], s))

    while pq:
        dst, now = heappop(pq)

        if dist[now] < dst: continue

        nxts = [(1, now + 1), (1, now - 1), (0, 2 * now)]
        for weight, nxt in nxts:
            if 0 <= nxt <= 100000:
                shortest = dist[now] + weight
                if shortest < dist[nxt]:
                    dist[nxt] = shortest
                    heappush(pq, (shortest, nxt))
    return dist


n, k = map(int, input().split())

print(dijkstra(n)[k])