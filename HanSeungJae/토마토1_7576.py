from collections import deque
import sys
input = sys.stdin.readline

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs():
    q = deque()
    cnt = -1

    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                q.append((i, j))

    while q:
        r = len(q)

        for _ in range(r):
            ci, cj = q.popleft()

            for k in range(4):
                ni = ci + di[k]
                nj = cj + dj[k]

                if 0 <= ni < n and 0 <= nj < m and box[ni][nj] == 0:
                    box[ni][nj] = 1
                    q.append((ni, nj))
        cnt += 1
    
    for i in range(n):
        if 0 in box[i]:
            return -1
    return cnt


m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

answer = bfs()

print(answer)