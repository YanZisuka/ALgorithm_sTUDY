import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def dfs(ci, cj):
    if dp[ci][cj]:
        return dp[ci][cj]

    dp[ci][cj] = 1

    for k in range(4):
        ni = ci + di[k]
        nj = cj + dj[k]

        if 0 <= ni < n and 0 <= nj < n and board[ni][nj] > board[ci][cj]:
            dp[ci][cj] = max(dp[ci][cj], dfs(ni, nj) + 1)
    return dp[ci][cj]


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))

print(answer)
