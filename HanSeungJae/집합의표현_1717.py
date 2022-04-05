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


n, m = map(int, input().split())
parents = [i for i in range(n+1)]

for _ in range(m):
    operator, a, b = map(int, input().split())
    if operator == 0:
        union(a, b)
    else:
        if find(a) != find(b):
            print('NO')
        else:
            print('YES')