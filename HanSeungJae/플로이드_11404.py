import sys
input = sys.stdin.readline


def floyd():
    for md in range(1, n+1):
        for s in range(1, n+1):
            for e in range(1, n+1):
                if dist[s][e] > dist[s][md] + dist[md][e]:
                    dist[s][e] = dist[s][md] + dist[md][e]


n = int(input())
m = int(input())
dist = [[float('inf')] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if dist[a][b] > c:
        dist[a][b] = c

floyd()

for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] < float('inf'):
            print(dist[i][j], end=' ')
        else:
            print(0, end=' ')
    if i != n:
        print()