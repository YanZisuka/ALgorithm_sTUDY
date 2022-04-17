import sys
input = sys.stdin.readline


n, m = map(int, input().split())
dp = [[[0] + [-float('inf')] * m for _ in range(n+1)] for _ in range(2)]  # dp[0] = 전 인덱스 제외, dp[1] = 전 인덱스 포함

for i in range(1, n+1):
    num = int(input())
    for j in range(1, min(m, (i+1) // 2) + 1):
        dp[0][i][j] = max(dp[1][i-1][j], dp[0][i-1][j])
        dp[1][i][j] = max(dp[1][i-1][j], dp[0][i-1][j-1]) + num

print(max(dp[0][n][m], dp[1][n][m]))