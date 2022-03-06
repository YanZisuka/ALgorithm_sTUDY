def dfs(start_row, start_col):
    stack = []
    stack.append([start_row,start_col])
    mat[start_row][start_col] = '0'
    cnt = 1

    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <N and 0 <= ny <N and mat[nx][ny] == '1':
                stack.append([nx,ny])
                mat[nx][ny] = '0'
                cnt += 1
    return cnt


N = int(input())
mat = [list(input()) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0 ,-1]

result = []
for row in range(N):
    for col in range(N):
        if mat[row][col] == '1':
            result.append(dfs(row,col))

result.sort()
print(len(result))
for num in result:
    print(num)