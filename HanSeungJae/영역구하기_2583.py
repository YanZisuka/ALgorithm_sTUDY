import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    board[si][sj] = 2
    cnt = 1

    while q:
        ci, cj = q.popleft()
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 0:
                board[ni][nj] = 2
                cnt += 1
                q.append((ni, nj))
    return cnt


def draw(st, en):
    for i in range(st[0], en[0], -1):
        for j in range(st[1], en[1]):
            board[i][j] = 1


def conv(x, y):
    i = m - y - 1
    j = x
    return (i, j)


m, n, k = map(int, input().split())
board = [[0] * n for _ in range(m)]
rects = []
answer = []
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    st = conv(x1, y1)
    en = conv(x2, y2)
    rects.append((st, en))

for r in rects:
    draw(*r)

for i in range(m):
    for j in range(n):
        if not board[i][j]:
            answer.append(bfs(i, j))

answer.sort()
print(len(answer))
for a in answer:
    print(a, end=' ')