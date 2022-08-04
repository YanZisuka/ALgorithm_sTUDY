import sys
def input(): return sys.stdin.readline().strip()


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
    global cost

    for e in edges:
        a, b, c = e
        if find(a) != find(b):
            union(a, b)
            cost += c


n, m = map(int, input().split())
parents = [i for i in range(n+1)]
nodes = [0]
edges = []
cost = 0

for _ in range(n):
    x, y = map(int, input().split())
    nodes.append((x, y))

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

for i in range(1, n+1):
    for j in range(i+1, n+1):
        a, b = nodes[i], nodes[j]
        c = (abs(a[0] - b[0]) ** 2 + abs(a[1] - b[1]) ** 2) ** 0.5
        edges.append((i, j, c))

edges.sort(key=lambda x: x[2])
kruskal()

print(f'{cost:.2f}')
