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
    edges.sort(key=lambda x: x[2])

    for i in range(len(edges)):
        a, b, c = edges[i]
        if find(a) != find(b):
            union(a, b)
            links.append((a, b, c))
            answer += c


n, m = map(int, input().split())
edges = []
parents = [i for i in range(n+1)]
links = []
answer = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

kruskal()
answer -= links[-1][2]
print(answer)