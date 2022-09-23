def solution(board, skill):
    answer = 0
    tmp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    for type, r1, c1, r2, c2, deg in skill:
        tmp[r1][c1] += deg if type == 2 else -deg
        tmp[r1][c2 + 1] += -deg if type == 2 else deg
        tmp[r2 + 1][c1] += -deg if type == 2 else deg
        tmp[r2 + 1][c2 + 1] += deg if type == 2 else -deg

    for i in range(len(tmp) - 1):
        for j in range(len(tmp[0]) - 1):
            tmp[i][j + 1] += tmp[i][j]

    for j in range(len(tmp[0]) - 1):
        for i in range(len(tmp) - 1):
            tmp[i + 1][j] += tmp[i][j]

    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += tmp[i][j]
            if board[i][j] > 0: answer += 1
    return answer