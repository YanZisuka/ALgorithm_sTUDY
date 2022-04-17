def dfs(row, col):
    d_row = [-1, 1, 0, 0]
    d_col = [0, 0, -1, 1]

    if dp[row][col]:
        return dp[row][col]

    dp[row][col] = 1

    for i in range(4):
        n_row = row + d_row[i]
        n_col = col + d_col[i]

        if 0 <= n_row < N and 0 <= n_col < N and forest[row][col] < forest[n_row][n_col]:
            dp[row][col] = max(dp[row][col], dfs(n_row, n_col) + 1)

    return dp[row][col]


N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
answer = 0

for row in range(N):
    for col in range(N):
        answer = max(answer, dfs(row, col))

print(answer)