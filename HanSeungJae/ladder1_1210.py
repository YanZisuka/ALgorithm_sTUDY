import sys
sys.stdin = open('input.txt')


def set_board():
    board = [list(map(int, input().split())) for _ in range(100)]
    return board


def find_ladder_sol(board):
    i = len(board)-1
    j = board[i].index(2)

    while True:
        i -= 1
        
        if 0 <= j - 1 < 100 and board[i][j - 1] == 1:
            while 0 <= j - 1 < 100 and board[i][j - 1] == 1:
                j -= 1
            continue

        if 0 <= j + 1 < 100 and board[i][j + 1] == 1:
            while 0 <= j + 1 < 100 and board[i][j + 1] == 1:
                j += 1
            continue

        if i == 0:
            return j


for tc in range(1, 11):
    n = int(input())
    board = set_board()
    
    print(f'#{tc} {find_ladder_sol(board)}')