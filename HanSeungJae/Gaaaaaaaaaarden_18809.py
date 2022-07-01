import sys
from collections import deque
from itertools import combinations
input = lambda: sys.stdin.readline().strip()

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(greens, reds):
    visited = [[0] * m for _ in range(n)]
    q = deque()
    cnt = 0

    for i, j in greens:
        q.append((i, j, -1))
        visited[i][j] = -1
    for i, j in reds:
        q.append((i, j, -2))
        visited[i][j] = -2

    while q:
        r = len(q)
        for _ in range(r):
            ci, cj, color = q.popleft()

            if visited[ci][cj] == -3: continue

            for k in range(4):
                ni = ci + di[k]
                nj = cj + dj[k]

                if 0 <= ni < n and 0 <= nj < m and (board[ni][nj] == 1 or board[ni][nj] == 2) and visited[ni][nj] == 0:
                    visited[ni][nj] = -color
                    q.append((ni, nj, color))
                elif 0 <= ni < n and 0 <= nj < m and (board[ni][nj] == 1 or board[ni][nj] == 2) and visited[ni][nj] == 1 and color == -2:
                    visited[ni][nj] = -3
                    cnt += 1
                elif 0 <= ni < n and 0 <= nj < m and (board[ni][nj] == 1 or board[ni][nj] == 2) and visited[ni][nj] == 2 and color == -1:
                    visited[ni][nj] = -3
                    cnt += 1
        
        for i in range(n):
            for j in range(m):
                if visited[i][j] > 0:
                    visited[i][j] *= -1
    return cnt


n, m, gs, rs = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
lands = []
answer = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            lands.append((i, j))

landset = set(lands)
for gcase in combinations(lands, gs):
    redset = list(landset - set(gcase))
    greens = list(gcase)
    for rcase in combinations(redset, rs):
        reds = list(rcase)
        answer = max(answer, bfs(greens, reds))
print(answer)