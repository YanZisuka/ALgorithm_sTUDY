from collections import deque
import sys
input = sys.stdin.readline

di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]
d_left = [(-1, 1, 0.01),
          (1, 1, 0.01),
          (-1, 0, 0.07),
          (1, 0, 0.07),
          (-2, 0, 0.02),
          (2, 0, 0.02),
          (-1, -1, 0.10),
          (1, -1, 0.10),
          (0, -2, 0.05),
          (0, -1, 0.55),]
d_right = [(-1, -1, 0.01),
           (1, -1, 0.01),
           (-1, 0, 0.07),
           (1, 0, 0.07),
           (-2, 0, 0.02),
           (2, 0, 0.02),
           (-1, 1, 0.10),
           (1, 1, 0.10),
           (0, 2, 0.05),
           (0, 1, 0.55)]
d_up = [(1, -1, 0.01),
        (1, 1, 0.01),
        (0, -1, 0.07),
        (0, 1, 0.07),
        (0, -2, 0.02),
        (0, 2, 0.02),
        (-1, -1, 0.10),
        (-1, 1, 0.10),
        (-2, 0, 0.05),
        (-1, 0, 0.55)]
d_down = [(-1, -1, 0.01),
          (-1, 1, 0.01),
          (0, -1, 0.07),
          (0, 1, 0.07),
          (0, -2, 0.02),
          (0, 2, 0.02),
          (1, -1, 0.10),
          (1, 1, 0.10),
          (2, 0, 0.05),
          (1, 0, 0.55)]


def tornado():
    i, j = n//2, n//2
    momentum = 0
    
    while True:
        for k in range(4):
            if k % 2 == 0:
                momentum += 1
            for l in range(momentum):
                i = i + di[k]
                j = j + dj[k]
                if 0 <= i < n and 0 <= j < n:
                    boardIdx.append((i, j, k))
                if (i, j) == (0, 0):
                    return
                

def storm(i, j, k):
    global answer
    temp = 0
    
    if k == 0:
        dir = d_left
    elif k == 1:
        dir = d_down
    elif k == 2:
        dir = d_right
    else:
        dir = d_up
    
    # ratio
    for l in range(9):
        di = dir[l][0]
        dj = dir[l][1]
        ratio = dir[l][2]
        
        ni = i + di
        nj = j + dj
        if 0 <= ni < n and 0 <= nj < n:
            board[ni][nj] += int(board[i][j] * ratio)
            temp += int(board[i][j] * ratio)
        else:
            answer += int(board[i][j] * ratio)
            temp += int(board[i][j] * ratio)
    
    # alpha
    ni = i + dir[9][0]
    nj = j + dir[9][1]
    if 0 <= ni < n and 0 <= nj < n:
        board[ni][nj] += board[i][j] - temp
        board[i][j] = 0
    else:
        answer += board[i][j] - temp
        board[i][j] = 0


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0
boardIdx = deque()
tornado()

while boardIdx:
    i, j, k = boardIdx.popleft()
    storm(i, j, k)

print(answer)