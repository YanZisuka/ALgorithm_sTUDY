import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()


def bfs(st, group):
    q = deque([st])
    visited[st] = group
    while q:
        c = q.popleft()

        for n in graph[c]:
            if not visited[n]:
                q.append(n)
                visited[n] = -1 * visited[c]
            elif visited[n] == visited[c]:
                return False
    return True


k = int(input())
for tc in range(1, k + 1):
    (V, E) = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        (u, v) = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, V + 1):
        if not visited[i]:
            result = bfs(i, 1)
            if not result:
                break

    print("YES" if result else "NO")
