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
edges = []
for _ in range(m+1):
    a, b, c = map(int, input().split())
    c = 0 if c else 1
    edges.append((a, b, c))

for i in range(2):
    parents = [i for i in range(n+1)]
    cost = 0

    if i == 0:
        edges.sort(key=lambda x: x[2])
    else:
        edges.sort(key=lambda x: -x[2])

    kruskal()

    if i == 0:
        min_cost = cost

print(cost ** 2 - min_cost ** 2)
