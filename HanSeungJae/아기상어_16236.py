import sys
from collections import deque
input = sys.stdin.readline

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(i, j):
    visited = [[False] * n for _ in range(n)]
    feed = []
    q = deque()
    q.append((i, j, 0))
    visited[i][j] = True
    minDist = float('inf')

    while q:
        i, j, dist = q.popleft()
        
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                if board[ni][nj] <= babySize:
                    visited[ni][nj] = True
                    if 0 < board[ni][nj] < babySize:
                        minDist = dist
                        feed.append((ni, nj, dist+1))
                    if dist+1 <= minDist:
                        q.append((ni, nj, dist+1))

    if feed:
        feed.sort(key=lambda x: (x[2], x[0], x[1]))
        return feed[0]
    return 0


def hunt(feed):
    global answer, babySize, sizeUpCnt, sharkPos, fishCnt

    ni, nj = feed[0], feed[1]
    board[ni][nj] = 0
    sharkPos = (ni, nj)
    answer += feed[2]
    sizeUpCnt += 1
    fishCnt -= 1

    if sizeUpCnt == babySize:
        babySize += 1
        sizeUpCnt = 0


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
fishCnt = 0
babySize = 2
sizeUpCnt = 0
answer = 0

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            sharkPos = (i, j)
        if 0 < board[i][j] < 7:
            fishCnt += 1

board[sharkPos[0]][sharkPos[1]] = 0

while fishCnt:
    feed = bfs(*sharkPos)
    
    if not feed:
        break

    hunt(feed)
    
print(answer)