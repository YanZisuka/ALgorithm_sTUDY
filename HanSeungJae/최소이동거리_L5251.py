from heapq import *
import sys
sys.stdin = open('input.txt')


def dijkstra(s):
    dist = [float('inf')] * (n+1)
    dist[s] = 0
    heap = []
    heappush(heap, (dist[0], s))
    
    while heap:
        dst, now = heappop(heap)
        
        if dist[now] < dst:
            continue
            
        for nxt, weight in graph[now]:
            shortest = dist[now] + weight
            if shortest < dist[nxt]:
                dist[nxt] = shortest
                heappush(heap, (shortest, nxt))
                
    return dist


t = int(input())
for tc in range(1, t+1):
    n, e = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        
    dist = dijkstra(0)
    
    print(f'#{tc} {dist[n]}')