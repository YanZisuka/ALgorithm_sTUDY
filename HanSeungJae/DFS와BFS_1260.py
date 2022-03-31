from collections import deque
import sys
input = sys.stdin.readline


def dfs(v):
    visited[v] = True
    ans.append(v)

    if not graph[v]:
        return

    for next in graph[v]:
        if not visited[next]:
            dfs(next)


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        node = queue.popleft()
        ans.append(node)

        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
            

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for i in range(n+1):
    graph[i].sort()

for i in range(2):
    ans = []
    visited = [False] * (n+1)
    visited[0] = True
    if i % 2 == 0:
        dfs(v)
    else:
        bfs(v)
    print(' '.join(map(str, ans)))
