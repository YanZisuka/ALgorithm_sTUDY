import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()


def bfs(a, b):
    visited = [None] + [0] * n
    q = deque()
    q.append((a, 0))
    visited[a] = 1

    while q:
        (now, d) = q.popleft()
        if now == b:
            return d
        for (nxt, dist) in tree[now]:
            if not visited[nxt]:
                visited[nxt] = 1
                q.append((nxt, d + dist))


n, m = map(int, input().split())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

seekers = []
for _ in range(m):
    a, b = map(int, input().split())
    seekers.append((a, b))

for (a, b) in seekers:
    print(bfs(a, b))
