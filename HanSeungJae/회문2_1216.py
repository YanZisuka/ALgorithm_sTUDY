import sys
sys.stdin = open('input.txt')


def set_board():
    board = [list(input()) for _ in range(100)]
    return board


def isPalindrome(word):
    if word == word[::-1]:
        return True
    return False


def get_longest_on_row(board):
    max_cnt = 1
    for i in range(100):
        for m in range(100, 1, -1):
            j = 0
            if m < max_cnt:
                break
            while True:
                if j+m > 100:
                    break
                if isPalindrome("".join(board[i][j:j+m])):
                    max_cnt = m
                    break
                j += 1
    return max_cnt


def get_longest_on_col(board):
    for i in range(100):
        for j in range(100):
            if i > j:
                board[i][j], board[j][i] = board[j][i], board[i][j]
    max_cnt = 1
    for i in range(100):
        for m in range(100, 1, -1):
            j = 0
            if m < max_cnt:
                break
            while True:
                if j+m > 100:
                    break
                if isPalindrome("".join(board[i][j:j + m])):
                    max_cnt = m
                    break
                j += 1
    return max_cnt


def find_the_longest_Palindrome(board):
    length = []
    length.append(get_longest_on_row(board))
    length.append(get_longest_on_col(board))
    return max(length)
        

for tc in range(1, 11):
    n = int(input())
    board = set_board()
    
    print(f'#{tc} {find_the_longest_Palindrome(board)}')
    