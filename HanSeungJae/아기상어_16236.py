import sys
from collections import deque
input = sys.stdin.readline

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(i, j):
    dist = [[0] * n for _ in range(n)]
    feed = []
    q = deque()
    q.append((i, j))
    dist[i][j] = 1
    cnt = 2

    while q:
        r = len(q)
        for _ in range(r):
            i, j = q.popleft()
            
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                
                if 0 <= ni < n and 0 <= nj < n and dist[ni][nj] == 0:
                    if board[ni][nj] <= babySize:
                        dist[ni][nj] = cnt
                        q.append((ni, nj))
                    if 0 < board[ni][nj] < babySize:
                        feed.append((ni, nj, dist[ni][nj]-1))
        if feed:
            feed.sort(key=lambda x: (x[2], x[0], x[1]))
            return feed[0]
        cnt += 1

    return 0


def hunt(feed, i, j):
    global answer, babySize, sizeUpCnt, sharkPos

    ni, nj = feed[0], feed[1]
    board[i][j] = 0
    board[ni][nj] = 9
    sharkPos = (ni, nj)
    answer += feed[2]
    sizeUpCnt += 1

    if sizeUpCnt == babySize:
        babySize += 1
        sizeUpCnt = 0


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
babySize = 2
sizeUpCnt = 0
answer = 0

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            sharkPos = (i, j)

while True:
    feed = bfs(*sharkPos)

    if not feed:
        break

    hunt(feed, *sharkPos)
    
print(answer)