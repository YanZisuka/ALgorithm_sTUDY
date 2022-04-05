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


n = int(input())
m = int(input())
parents = [i for i in range(n)]
cnt = 0

for i in range(n):
    st = list(map(int, input().split()))
    for j in range(len(st)):
        if st[j] == 1:
            union(i, j)

plan = list(map(int, input().split()))

for i in range(m):
    if find(plan[i]-1) != find(plan[i-1]-1):
        print('NO')
        cnt += 1
        break

if cnt == 0:
    print('YES')