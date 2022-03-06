N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(i, j):
    global cnt
    if i < 0 or j < 0 or i >= N or j >= N:
        return False

    if matrix[i][j] == 1:
        cnt += 1
        matrix[i][j] = 0
        for k in range(4):
            dfs(i+dx[k], j+dy[k])
        return True


group = []
cnt = 0

for i in range(N):
    for j in range(N):
        if dfs(i, j):
            group.append(cnt)
            cnt = 0

group.sort()
print(len(group))
for num in group:
    print(num)
