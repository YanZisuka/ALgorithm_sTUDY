import sys
input = sys.stdin.readline


def find(v):
    if parents[v] != v:
        parents[v] = find(parents[v])
    return parents[v]


def union(v1, v2):
    a, b = find(v1), find(v2)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def kruskal():
    global answer

    for i in range(len(edges)):
        a, b, c = edges[i]

        if find(a) != find(b):
            union(a, b)
            answer += c


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
parents = [i for i in range(n)]
edges = []
answer = 0

for i in range(n):
    for j in range(i, n):
        a, b, c = i, j, board[i][j]
        edges.append((a, b, c))

edges.sort(key=lambda x: x[2])
kruskal()

print(answer)