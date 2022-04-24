from collections import deque
import sys
input = sys.stdin.readline

di = [-1, 1, 0, 0, 0, 0]
dj = [0, 0, -1, 1, 0, 0]
dk = [0, 0, 0, 0, -1, 1]


def bfs():
    q = deque()
    cnt = -1

    for start in starts:
        q.append(start)

    while q:
        r = len(q)
        for _ in range(r):
            ck, ci, cj = q.popleft()

            for k in range(6):
                ni = ci + di[k]
                nj = cj + dj[k]
                nk = ck + dk[k]
                if 0 <= ni < n and 0 <= nj < m and 0 <= nk < h and box[nk][ni][nj] == 0:
                    box[nk][ni][nj] = 1
                    q.append((nk, ni, nj))
        cnt += 1

    for k in range(h):
        for i in range(n):
            if 0 in box[k][i]:
                return -1
    return cnt


m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
starts = []

for i in range(n):
    for j in range(m):
        for k in range(h):
            if box[k][i][j] == 1:
                starts.append((k, i, j))

answer = bfs()

print(answer)