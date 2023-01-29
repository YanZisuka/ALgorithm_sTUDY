import sys

input = lambda: sys.stdin.readline().strip()
INF = float("inf")

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

answer = INF

for k in range(3):
    dp = [[INF] * 3 for _ in range(n)]
    dp[0][k] = costs[0][k]

    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]

    for i in range(3):
        if i != k:
            answer = min(answer, dp[-1][i])

print(answer)
