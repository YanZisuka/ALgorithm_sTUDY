import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(i):
    visited[i] = True
    s = 0

    for next in graph[i][2]:
        if not visited[next]:
            s += dfs(next)

    if graph[i][0] == 'S':
        s += graph[i][1]

    elif graph[i][0] == 'W':
        s -= graph[i][1]
    
    if s <= 0:
        s = 0
    
    return s


n = int(input())
graph = [[0] * 3 for _ in range(n+1)]
for i in range(n+1):
    graph[i][2] = []
visited = [False] * (n+1)

i = 2
while i <= n:
    island = input().split()
    island[1] = int(island[1])
    island[2] = int(island[2])

    graph[i][0] = island[0]
    graph[i][1] = island[1]
    graph[island[2]][2].append(i)

    i += 1
ans = dfs(1)
print(ans)