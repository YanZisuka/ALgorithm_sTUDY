from math import *
import sys
input = sys.stdin.readline


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


n = int(input())
stars = []
edges = []
parents = [i for i in range(n)]
totalCost = 0

for _ in range(n):
    x, y = map(float, input().split())
    stars.append((x, y))

for i in range(n-1):
    for j in range(i+1, n):
        cost = sqrt(abs(stars[i][0]-stars[j][0])**2 + abs(stars[i][1]-stars[j][1])**2)
        edges.append((i, j, cost))

edges.sort(key=lambda x: x[2])
kruskal()

print(f'{totalCost:.2f}')
