import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()


def bfs(start: int) -> None:
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        now = q.popleft()

        for nxt in tree[now]:
            if not visited[nxt]:
                visited[nxt] = 1
                answer[nxt] = now
                q.append(nxt)


n = int(input())
tree = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
answer = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

bfs(1)

for i in range(2, n + 1):
    print(answer[i])
