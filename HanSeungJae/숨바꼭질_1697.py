import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


def bfs(si):
    q = deque()
    q.append((si, 0))
    visited[si] = 1

    while q:
        (ci, t) = q.popleft()

        if ci == k:
            return t

        for nxt in [ci - 1, ci + 1, 2 * ci]:
            if 0 <= nxt <= 100000 and not visited[nxt]:
                visited[nxt] = 1
                q.append((nxt, t + 1))


n, k = map(int, input().split())
visited = [0] * 100001
print(bfs(n))
