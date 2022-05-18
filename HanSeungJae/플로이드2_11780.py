import sys
input = sys.stdin.readline


def floyd():
    for md in range(1, n+1):
        for s in range(1, n+1):
            for e in range(1, n+1):
                if dist[s][e] > dist[s][md] + dist[md][e]:
                    dist[s][e] = dist[s][md] + dist[md][e]
                    nxt[s][e] = nxt[s][md]


n = int(input())
m = int(input())
dist = [[float('inf')] * (n+1) for _ in range(n+1)]
nxt = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if dist[a][b] > c:
        dist[a][b] = c
        nxt[a][b] = b

floyd()

for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] == float('inf'):
            dist[i][j] = 0

for i in range(1, n+1):
    print(*dist[i][1:])

for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] == 0:
            print(0)
            continue
        
        path = []
        st = i
        while st != j:
            path.append(st)
            st = nxt[st][j]
        path.append(j)
        print(len(path), end=' ')
        for node in path: print(node, end=' ')
        print()
        