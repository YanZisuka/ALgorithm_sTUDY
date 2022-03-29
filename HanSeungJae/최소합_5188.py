import sys
sys.stdin = open('input.txt')

di = [1, 0]
dj = [0, 1]


def dfs(step, i, j, score):
    global ans
    if step > n + (n-2):
        return
    if score >= ans:
        return
    if step == n + (n-2) and (i, j) == (n-1, n-1):
        ans = min(ans, score)
        return
    
    for k in range(2):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < n:
            dfs(step+1, ni, nj, score+board[ni][nj])


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    ans = float('inf')
    
    dfs(0, 0, 0, board[0][0])
    
    print(f'#{tc} {ans}')