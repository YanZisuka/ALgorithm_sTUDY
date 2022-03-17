import sys

sys.setrecursionlimit(100000)

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(i, j, rain):
    global cnt
    if i < 0 or j < 0 or i >= N or j >= N:
        return False

    if matrix[i][j] > rain and visit[i][j] == False:
        cnt += 1
        visit[i][j] = True
        for k in range(4):
            dfs(i + dx[k], j + dy[k], rain)
        return True


cnt = 0
safe_zone_number = []
safe_zone = []
visit = [list(False for _ in range(N)) for _ in range(N)]
max_rain = matrix[0][0]

for i in range(N):
    for j in range(N):
        if matrix[i][j] > max_rain:
            max_rain = matrix[i][j]

for rain in range(1, max_rain):
    for i in range(N):
        for j in range(N):
            if dfs(i, j, rain):
                safe_zone.append(cnt)
                cnt = 0
    safe_zone_number.append(len(safe_zone))
    safe_zone = []
    visit = [list(False for _ in range(N)) for _ in range(N)]

print(len(safe_zone_number))
