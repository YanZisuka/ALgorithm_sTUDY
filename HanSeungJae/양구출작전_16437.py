import sys
sys.setrecursionlimit(100000)

def dfs(i, w):
    visited[i] = True

    if graph[i][0] == 'S':
        if graph[i][1]-w >= 0:
            graph[1][1] += graph[i][1]-w
            w = 0
        else:
            w -= graph[i][1]
    elif graph[i][0] == 'W':
        w += graph[i][1]


    for next in graph[i][2]:
        if not visited[next]:
            dfs(next, w)


n = int(input())
graph = [[0] * 3 for _ in range(n+1)]
for i in range(n+1):
    graph[i][2] = []
visited = [False] * (n+1)

i = 2
while i <= n:
    island = input().split()
    island[1] = int(island[1])
    island[2] = [int(island[2])]

    graph[i][0] = island[0]
    graph[i][1] = island[1]
    graph[island[2][0]][2].append(i)

    i += 1
dfs(1, 0)
print(graph[1][1])