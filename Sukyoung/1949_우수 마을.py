import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x):
    visited[x] = 1
    pick[x][0] = population[x-1]
    for i in tree[x]:
        if visited[i] == 0:
            dfs(i)
            pick[x][0] += pick[i][1]
            pick[x][1] += max(pick[i][0],pick[i][1])

N = int(input())
population = list(map(int,input().split()))
pick = [[0,0] for _ in range(N+1)]
tree = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for i in range(N-1):
    U, V = map(int,input().split())
    tree[U].append(V)
    tree[V].append(U)

dfs(1)
print(max(pick[1]))