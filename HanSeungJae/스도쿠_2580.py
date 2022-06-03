import sys
input = sys.stdin.readline


def check_row(si, v):
    for j in range(9):
        if board[si][j] == v: return False
    return True


def check_col(sj, v):
    for i in range(9):
        if board[i][sj] == v: return False
    return True


def check_3x3(si, sj, v):
    ci, cj = si // 3 * 3, sj // 3 * 3
    for di in range(3):
        for dj in range(3):
            if board[ci+di][cj+dj] == v: return False
    return True


def dfs(step):

    if step == len(zeros):
        for i in range(9): print(*board[i])
        exit(0)

    ci, cj = zeros[step]

    for v in range(1, 10):
        if check_row(ci, v) and check_col(cj, v) and check_3x3(ci, cj, v):
            board[ci][cj] = v
            dfs(step + 1)
            board[ci][cj] = 0


board = [list(map(int, input().split())) for _ in range(9)]
zeros = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0: zeros.append((i, j))

dfs(0)
