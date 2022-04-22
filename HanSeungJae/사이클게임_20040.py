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

    
n, m = map(int, input().split())
parents = [i for i in range(n)]
answer = 0

for i in range(1, m+1):
    a, b = map(int, input().split())
    
    if find(a) == find(b):
        answer = i
        break

    union(a, b)

print(answer)