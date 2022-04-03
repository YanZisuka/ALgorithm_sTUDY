"""
PyPy3
"""
import sys
input = sys.stdin.readline


def floyd():
    for m in range(1, n+1):
        for s in range(1, n+1):
            for e in range(1, n+1):
                if dist[s][e] > dist[s][m] + dist[m][e]:
                    dist[s][e] = dist[s][m] + dist[m][e]

        
n, m = map(int, input().split())
dist = [[float('inf')] * (n+1) for _ in range(n+1)]
ans = 0

for i in range(1, n+1):
    dist[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    dist[a][b] = 1

floyd()

for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if dist[j][i] != float('inf') or dist[i][j] != float('inf'):
            cnt += 1
    if cnt == n:
        ans += 1

print(ans)