def solution(m, n, board):

    new_board = [[0] * m for _ in range(n)]  # 오른쪽으로 90도 회전
    for x in range(n):
        for y in range(m):
            new_board[x][y] = board[m - 1 - y][x]

    delete = []

    def is_sqr(x, y):
        if len(new_board[x]) > 1 and len(new_board[x + 1]) > y + 1:
            if new_board[x][y] == new_board[x][y + 1] and new_board[x][y] == new_board[x + 1][y] and new_board[x][y] == \
                    new_board[x + 1][y + 1]:
                delete.append([x, y])
                delete.append([x + 1, y])
                delete.append([x, y + 1])
                delete.append([x + 1, y + 1])

    cnt = 0
    while True:
        for x in range(n - 1):
            for y in range(len(new_board[x]) - 1):
                is_sqr(x, y)
        if not delete:
            break
        else:
            for d in delete:
                new_board[d[0]][d[1]] = 0

            for i in range(n):
                new_list = []
                for j in new_board[i]:
                    if j == 0:
                        cnt += 1
                    else:
                        new_list.append(j)
                new_board[i] = new_list

            delete = []

    answer = cnt
    return answer