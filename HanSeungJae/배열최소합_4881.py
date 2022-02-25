import sys
sys.stdin = open('input.txt')


def dfs(i, j, sum_val):
    visited_col[j] = True
    sum_val += board[i][j]
    global min_sum
    
    if sum_val >= min_sum:
        visited_col[j] = False
        return
    
    if i == n-1:
        if sum_val < min_sum:
            min_sum = sum_val
        visited_col[j] = False
        return
    
    for k in range(n):
        if not visited_col[k] and i < n-1:
            dfs(i+1, k, sum_val)
    visited_col[j] = False
    return


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited_col = [False] * n
    min_sum = float('inf')
    
    for j in range(n):
        # if board[0][j] == min(board[0]):
        dfs(0, j, 0)
    
    print(f'#{tc} {min_sum}')