from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    visited = [False] * (v+1)
    visited[0] = True
    q = deque()
    visited[start] = True
    q.append((start, 0))
    maxVal = (start, 0)
    
    while q:
        now, dist = q.popleft()
        for nxt, weight in tree[now]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, dist + weight))
                maxVal = max(maxVal, (nxt, dist + weight), key=lambda x: x[1])
    return maxVal


v = int(input())
tree = [[] for _ in range(v+1)]

for _ in range(v):
    st = list(map(int, input().split()))
    idx = 1
    while st[idx] != -1:
        if idx % 2:
            b = st[idx]
        else:
            c = st[idx]
            tree[st[0]].append((b, c))
        idx += 1

nde, dist = bfs(1)
nde, dist = bfs(nde)

print(dist)