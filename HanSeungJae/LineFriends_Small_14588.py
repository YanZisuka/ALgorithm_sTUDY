import sys
from itertools import combinations
input = sys.stdin.readline


def floyd():
    for m in range(1, n+1):
        for s in range(1, n+1):
            for e in range(1, n+1):
                if graph[s][e] > graph[s][m] + graph[m][e]:
                    graph[s][e] = graph[s][m] + graph[m][e]


INF = float('inf')
n = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0

lines = [list(map(int, input().split() + [i + 1])) for i in range(n)]
q = int(input())
qs = [list(map(int, input().split())) for _ in range(q)]

for l, r in combinations(lines, 2):
    if l[0] <= r[0] <= l[1] or r[0] <= l[0] <= r[1]:
        graph[l[2]][r[2]] = 1
        graph[r[2]][l[2]] = 1

floyd()

for query in qs:
    print(graph[query[0]][query[1]]) if graph[query[0]][query[1]] < INF else print(-1)