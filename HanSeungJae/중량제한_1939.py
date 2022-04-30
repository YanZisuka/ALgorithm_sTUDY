from collections import deque
import sys
input = sys.stdin.readline


def bfs(wght):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        cp = q.popleft()
        if cp == end:
            return True
        for np, cost in graph[cp]:
            if not visited[np] and wght <= cost:
                q.append(np)
                visited[np] = True
    return False


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for node in graph:
    node.sort(key=lambda x: -x[1])

start, end = map(int, input().split())
low, high = 1, 1000000000
while low <= high:
    visited = [False] * (n+1)
    mid = (low + high) // 2
    if bfs(mid):
        low = mid + 1
    else:
        high = mid - 1

print(high)