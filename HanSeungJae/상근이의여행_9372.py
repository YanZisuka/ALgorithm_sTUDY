import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


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


t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    edges = []
    parents = [i for i in range(n+1)]
    totalCost = 0

    for _ in range(m):
        a, b = map(int, input().split())
        edges.append((a, b, 1))

    kruskal()

    print(totalCost)