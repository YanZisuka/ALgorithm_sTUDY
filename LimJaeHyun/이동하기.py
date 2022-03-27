N, M = map(int, input().split())

maze = list(list(map(int, input().split())) for _ in range(N))
memo = list([0] * (M + 1) for _ in range(N + 1))

for i in range(1, N + 1):
    for j in range(1, M + 1):
        memo[i][j] = max(memo[i - 1][j], memo[i][j - 1], memo[i - 1][j - 1]) + maze[i - 1][j - 1]

print(memo[-1][-1])
