import sys
sys.stdin = open('input.txt')


def dfs(step, cnt, total, lst):
    global sol
    if cnt > c:
        return
    
    if step == m:
        if c >= cnt and sol < total:
            sol = total
        return

    dfs(step+1, cnt+lst[step], total+lst[step] ** 2, lst)
    dfs(step+1, cnt, total, lst)
    
    
t = int(input())
for tc in range(1, t + 1):
    n, m, c = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n-m+1):
            sol = 0
            dfs(0, 0, 0, board[i][j:j+m])
            dp[i][j] = sol
    
    for i1 in range(n):
        for j1 in range(n-m+1):
            for i2 in range(i1, n):
                sj = 0
                if i1 == i2:
                    sj = j1+m
                for j2 in range(sj, n-m+1):
                    ans = max(ans, dp[i1][j1] + dp[i2][j2])
            
    print(f'#{tc} {ans}')