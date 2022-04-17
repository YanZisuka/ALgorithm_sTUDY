import sys
input = sys.stdin.readline


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[[-float('inf')] * (m+2) for _ in range(n+1)] for _ in range(3)]
dp[0][1][0], dp[1][1][0], dp[2][1][0] = 0, 0, 0

for i in range(1, m+1):
    for k in range(3):
        dp[k][1][i] = dp[k][1][i-1] + board[0][i-1]

for i in range(2, n+1):
    for j in range(1, m+1):  # L -> R
        dp[0][i][j] = max(dp[0][i][j], dp[0][i-1][j] + board[i-1][j-1], dp[0][i][j-1] + board[i-1][j-1])
    for j in range(m, -1, -1):  # R -> L
        dp[1][i][j] = max(dp[1][i][j], dp[1][i-1][j] + board[i-1][j-1], dp[1][i][j+1] + board[i-1][j-1])
    for j in range(1, m+1):
        dp[2][i][j] = max(dp[0][i][j], dp[1][i][j])

    dp[0][i] = dp[2][i]
    dp[1][i] = dp[2][i]

print(dp[2][n][m])