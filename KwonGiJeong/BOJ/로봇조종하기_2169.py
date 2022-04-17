N, M = map(int, input().split())
mars = [list(map(int, input().split())) for _ in range(N)]

dp_left = [[0] * M for _ in range(N)]  # 왼쪽/위 중 큰 값
dp_right = [[0] * M for _ in range(N)]  # 오른쪽/위 중 큰 값
dp = [[0] * M for _ in range(N)]  # dp_left와 dp_right 중 큰 값

dp_left[0][0] = mars[0][0]
dp_right[0][0] = mars[0][0]
dp[0][0] = mars[0][0]

for col in range(1, M): # 윗쪽 모서리는 정해져 있음
    dp_left[0][col] = dp[0][col - 1] + mars[0][col]
    dp_right[0][col] = 0
    dp[0][col] = dp_left[0][col]

for row in range(1, N): # left는 왼쪽 모서리, right는 오른쪽 모서리가 정해져 있음
    dp_left[row][0] = dp[row - 1][0] + mars[row][0]
    dp_right[row][M - 1] = dp[row - 1][M - 1] + mars[row][M - 1]

    for col in range(1, M):
        dp_left[row][col] = max(dp_left[row][col - 1] + mars[row][col], dp[row - 1][col] + mars[row][col])
        dp_right[row][(M - 1) - col] = max(dp_right[row][(M - 1) - (col - 1)] + mars[row][(M - 1) - col], dp[row - 1][(M - 1) - col] + mars[row][(M - 1) - col])
        dp[row][col] = max(dp_left[row][col], dp_right[row][col])

    for col in range(M):
        dp[row][col] = max(dp_left[row][col], dp_right[row][col])

print(dp[N][M])