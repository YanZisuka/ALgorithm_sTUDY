import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


def find(v):
    if parents[v] != v:
        parents[v] = find(parents[v])
    return parents[v]


def union(v1, v2):
    a = find(v1)
    b = find(v2)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def kruskal():
    global totalCost

    for i in range(len(edges)):
        a, b, c = edges[i]

        if find(a) != find(b):
            union(a, b)
            totalCost += c


v, e = map(int, input().split())
parents = [i for i in range(v+1)]
edges = []
totalCost = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])
kruskal()

print(totalCost)
