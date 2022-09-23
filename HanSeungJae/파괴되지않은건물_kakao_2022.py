from pprint import pprint

def solution(board, skill):
    m, n = len(board), len(board[0])
    answer = 0
    tmp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    for type, r1, c1, r2, c2, deg in skill:
        tmp[r1][c1] += deg if type == 2 else -deg
        tmp[r1][c2 + 1] += -deg if type == 2 else deg
        tmp[r2 + 1][c1] += -deg if type == 2 else deg
        tmp[r2 + 1][c2 + 1] += deg if type == 2 else -deg

    for i in range(m):
        for j in range(n):
            tmp[i][j + 1] += tmp[i][j]

    for j in range(n):
        for i in range(m):
            tmp[i + 1][j] += tmp[i][j]

    for i in range(m):
        for j in range(n):
            board[i][j] += tmp[i][j]
            if board[i][j] > 0: answer += 1
    return answer





print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])) # 10
print(solution([[1,2,3],[4,5,6],[7,8,9]],[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]])) # 6
