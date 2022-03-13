import sys
input = sys.stdin.readline

di = [-1, 0, -1]
dj = [0, -1, -1]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
memo = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        memo[i][j] = arr[i][j]
        for k in range(2):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                memo[i][j] += memo[ni][nj]

        ni = i + di[2]
        nj = j + dj[2]
        if 0 <= ni and 0 <= nj:
            memo[i][j] -= memo[ni][nj]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

    ans = memo[x2][y2]
    if x1-1 >= 0:
        ans -= memo[x1-1][y2]
    if y1-1 >= 0:
        ans -= memo[x2][y1-1]
    if x1-1 >= 0 and y1-1 >= 0:
        ans += memo[x1-1][y1-1]
    
    print(ans)
