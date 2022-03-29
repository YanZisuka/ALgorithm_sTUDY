from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def iscombo(i, j):
    visited = [[False] * 6 for _ in range(12)]
    color = board[i][j]
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    cnt = 0
    
    while q:
        i, j = q.popleft()
        cnt += 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < 12 and 0 <= nj < 6:
                if not visited[ni][nj] and board[ni][nj] == color:
                    visited[ni][nj] = True
                    q.append((ni, nj))
    
    if cnt >= 4:
        return True
    
    return False


def combo(i, j):
    color = board[i][j]
    q = deque()
    q.append((i, j))
    
    while q:
        i, j = q.popleft()
        board[i][j] = '.'
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < 12 and 0 <= nj < 6:
                if board[ni][nj] != '.' and board[ni][nj] == color:
                    q.append((ni, nj))


def gravity():
    for j in range(6):
        dotCnt = 0
        for i in range(11, -1, -1):
            if board[i][j] == '.':
                dotCnt += 1
            elif board[i][j] != '.':
                board[i][j], board[i+dotCnt][j] = board[i+dotCnt][j], board[i][j] 


board = [list(input()) for _ in range(12)]
comboCount = 0
while True:
    cnt = 0
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.':
                if iscombo(i, j):
                    cnt += 1
                    combo(i, j)
    
    if cnt == 0:
        break

    comboCount += 1
    gravity()

print(comboCount)
