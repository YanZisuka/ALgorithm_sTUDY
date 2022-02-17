import sys
sys.stdin = open('input.txt')


def set_board(n):
    board = [list(input()) for _ in range(n)]
    return board


def isPalindrome(word):
    if word == word[::-1]:
        return True
    return False


def get_pal_on_row(n, m, board):
    for i in range(n):
        j = 0
        while True:
            if j+m > n:
                break
            if isPalindrome("".join(board[i][j:j+m])):
                return "".join(board[i][j:j+m])
            j += 1


def get_pal_on_col(n, m, board):
    for i in range(n):
        for j in range(n):
            if i > j:
                board[i][j], board[j][i] = board[j][i], board[i][j]
    for i in range(n):
        j = 0
        while True:
            if j+m > n:
                break
            if isPalindrome("".join(board[i][j:j+m])):
                return "".join(board[i][j:j+m])
            j += 1


def findPalindrome(n, m, board):
    if get_pal_on_row(n, m, board): return get_pal_on_row(n, m, board)
    return get_pal_on_col(n, m, board)


t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    board = set_board(n)

    print(f'#{tc} {findPalindrome(n, m, board)}')
