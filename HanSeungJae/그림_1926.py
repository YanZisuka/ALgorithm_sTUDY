import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    size = 1

    while q:
        ci, cj = q.popleft()

        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == 1 and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni, nj))
                size += 1

    return size


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
paints = []

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            paints.append(bfs(i, j))

maxv = max(paints) if paints else 0
print(len(paints), maxv, sep='\n')
