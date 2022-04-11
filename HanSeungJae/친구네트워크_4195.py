import sys
input = sys.stdin.readline


def find(v):
    if parents[v] != v:
        parents[v] = find(parents[v])
    return parents[v]


def union(v1, v2):
    a = find(v1)
    b = find(v2)

    if a != b:
        parents[b] = a
        sizes[a] += sizes[b]


t = int(input())
for tc in range(1, t+1):
    parents = {}
    sizes = {}

    f = int(input())
    for _ in range(f):
        candidate = []
        a, b = input().strip().split()

        if not parents.get(a):
            parents[a] = a
            sizes[a] = 1
        if not parents.get(b):
            parents[b] = b
            sizes[b] = 1

        union(a, b)
        
        print(sizes[find(a)])
