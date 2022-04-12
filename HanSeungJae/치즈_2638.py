from collections import deque
import sys
input = sys.stdin.readline

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(si, sj):
    visited = [[False] * m for _ in range(n)]
    q = deque()
    visited[si][sj] = True
    q.append((si, sj))

    while q:
        ci, cj = q.popleft()

        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]

            if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == 0 and not visited[ni][nj]:
                visited[ni][nj] = True
                q.append((ni, nj))
            if 0 <= ni < n and 0 <= nj < m and board[ni][nj] != 0:
                board[ni][nj] += 1


def melt():
    global cnt

    for i in range(n):
        for j in range(m):
            if board[i][j] > 2:
                board[i][j] = 0
                cnt -= 1
            elif 0 < board[i][j] <= 2:
                board[i][j] = 1


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
answer = 0

for i in range(n):
    cnt += board[i].count(1)

while cnt:
    bfs(0, 0)
    answer += 1
    melt()

print(answer)