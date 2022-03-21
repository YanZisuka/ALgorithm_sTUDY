import sys, copy
input = sys.stdin.readline

di = [0, -1, -1]
dj = [-1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dp = copy.deepcopy(board)

for i in range(n):
    for j in range(m):
        for k in range(3):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < n and 0 <= nj < m:
                dp[i][j] = max(dp[i][j], board[i][j] + dp[ni][nj])

print(dp[n-1][m-1])
