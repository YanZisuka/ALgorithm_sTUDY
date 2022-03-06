from copy import deepcopy

def dfs(dfsmat,start_row, start_col):
    stack = []
    stack.append([start_row,start_col])
    dfsmat[start_row][start_col] = 0

    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <N and 0 <= ny <N and dfsmat[nx][ny] != 0:
                stack.append([nx,ny])
                dfsmat[nx][ny] = 0


N = int(input())
mat = [list(map(int,input().split())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0 ,-1]

max_value = max(map(max,mat)) # 가장 높은 지역 찾기


result = [0,]
for i in range(0,max_value+1): # 비의 높이보다 낮은 지역은 0으로
    new_mat = deepcopy(mat)
    for row in range(N):
        for col in range(N):
            if new_mat[row][col] <= i:
                new_mat[row][col] = 0

    cnt = 0  # 영역 개수 세기
    for row in range(N):
        for col in range(N):
            if new_mat[row][col] != 0:
                dfs(new_mat,row,col)
                cnt+=1
    result.append(cnt)

print(max(result))