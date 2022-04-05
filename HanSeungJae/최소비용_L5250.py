from heapq import *
import sys
sys.stdin = open('input.txt')

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def dijkstra(i, j):
    dist = [[float('inf')] * n for _ in range(n)]
    dist[i][j] = 0
    heap = []
    heappush(heap, (dist[i][j], (i, j)))
    
    while heap:
        dst, (ci, cj) = heappop(heap)
        
        if dist[ci][cj] < dst:
            continue
        
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                
                if board[ni][nj] > board[ci][cj]:  # 다음 지대가 더 높은 경우
                    weight = 1 + board[ni][nj] - board[ci][cj]
                else:
                    weight = 1
                    
                shortest = dist[ci][cj] + weight
                if shortest < dist[ni][nj]:
                    dist[ni][nj] = shortest
                    heappush(heap, (shortest, (ni, nj)))
    return dist


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    dist = dijkstra(0, 0)
    
    print(f'#{tc} {dist[n-1][n-1]}')