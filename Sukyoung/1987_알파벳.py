def dfs(x, y):
    global word
    word.append(mat[x][y])

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C:
            if mat[nx][ny] not in word:
                dfs(nx,ny)


    return word

R, C = map(int,input().split())
mat = [list(input()) for _ in range(R)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[0]*C for _ in range(R)]
word = [mat[0][0]]
print(dfs(1,0))
word = [mat[0][0]]
print(dfs(0,1))






