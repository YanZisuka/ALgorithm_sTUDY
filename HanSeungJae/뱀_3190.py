import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def get_dir(dir, c):
    if c == "L":
        if dir == 3:
            return 0
        if dir == 2:
            return 1
        if dir == 1:
            return 3
        return 2
    if c == "D":
        if dir == 3:
            return 1
        if dir == 2:
            return 0
        if dir == 1:
            return 2
        return 3


def head(snake):
    return snake[0]


def dummy():
    snake = deque()
    snake.append((0, 0))
    dir = 3
    sec = 0

    while 1:
        for control in controls:
            (x, c) = control
            if x == sec:
                dir = get_dir(dir, c)

        for body in snake:
            (i, j) = body
            board[i][j] = 2

        (ci, cj) = head(snake)

        ni = ci + di[dir]
        nj = cj + dj[dir]

        sec += 1

        if 0 <= ni < n and 0 <= nj < n and board[ni][nj] == 0:
            for body in snake:
                (i, j) = body
                board[i][j] = 0
            snake.appendleft((ni, nj))
            snake.pop()
        elif 0 <= ni < n and 0 <= nj < n and board[ni][nj] == 1:
            for body in snake:
                (i, j) = body
                board[i][j] = 0
            snake.appendleft((ni, nj))
        elif 0 <= ni < n and 0 <= nj < n and board[ni][nj] == 2:
            return sec
        else:
            return sec
    return


n = int(input())
board = [[0] * n for _ in range(n)]
k = int(input())
for _ in range(k):
    (i, j) = map(int, input().split())
    board[i - 1][j - 1] = 1
l = int(input())
controls = []
for _ in range(l):
    (x, c) = input().split()
    x = int(x)
    controls.append((x, c))

print(dummy())
