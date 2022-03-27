N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (M + 1) for _ in range(N + 1)]

for row in range(1, N + 1):
    for col in range(1, M + 1):
        dp[row][col] = maze[row - 1][col - 1] + max(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1])

print(dp[N][M])