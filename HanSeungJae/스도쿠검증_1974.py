import sys
sys.stdin = open('input.txt')


def set_board(n):
    board = [list(map(int, input().split())) for _ in range(n)]
    return board


def check_row(n, board):
    for i in range(n):
        cnt_list = []
        for num in range(1, 10):
            cnt_list.append(board[i].count(num))
        for j in range(9):
            if cnt_list[j] != 1:
                return 0
    return 1
        

def check_col(n, board):
    for i in range(n):
        for j in range(n):
            if i > j:
                board[i][j], board[j][i] = board[j][i], board[i][j]
                
    for i in range(n):
        cnt_list = []
        for num in range(1, 10):
            cnt_list.append(board[i].count(num))
        for j in range(9):
            if cnt_list[j] != 1:
                return 0
    return 1


def check_3x3(m, l, board):
    cnt_list = []
    
    for i in range(m, m+3):
        for j in range(l, l+3):
            cnt_list.append(board[i][j])
            
    for num in range(1, 10):
        if cnt_list.count(num) != 1:
            return 0
    return 1


def verification_sudoku(n, board):
    if check_row(n, board) == 0:
        return 0
    if check_col(n, board) == 0:
        return 0
    for m in range(0, 9, 3):
        for l in range(0, 9, 3):
            if check_3x3(m, l, board) == 0:
                return 0
    return 1


t = int(input())
for tc in range(1, t+1):
    n = 9
    board = set_board(n)
    
    print(f'#{tc} {verification_sudoku(n, board)}')
    