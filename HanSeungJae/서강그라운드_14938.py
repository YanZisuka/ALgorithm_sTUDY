import sys
input = sys.stdin.readline


def floyd():
    for m in range(1, n+1):
        for s in range(1, n+1):
            for e in range(1, n+1):
                if adj[s][m] + adj[m][e] < adj[s][e]:
                    adj[s][e] = adj[s][m] + adj[m][e]


n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
adj = [[float('inf')] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    adj[i][i] = 0

answers = [0] * (n+1)

for _ in range(r):
    a, b, c = map(int, input().split())
    adj[a][b] = c
    adj[b][a] = c

floyd()

for i in range(1, n+1):
    for j in range(1, n+1):
        if adj[i][j] <= m:
            answers[i] += items[j]

print(max(answers))