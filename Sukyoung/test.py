from itertools import combinations
from copy import deepcopy
from collections import deque


# 1.bfs
def bfs(mat,start_row,start_col):
    queue = deque()
    queue.append([start_row,start_col])


    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<=ny<M and mat[nx][ny] == '0':
                mat[nx][ny]='2'
                queue.append([nx,ny])



N , M = map(int,input().split())
mat = [input().split() for _ in range(N)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
# 2.벽 세우기
wall = []
for row in range(N):
    for col in range(M):
        if mat[row][col] == '0':
            wall.append([row,col])
wall_ok = list(combinations(wall,3))

answer = []
for w in wall_ok:
    new_mat = deepcopy(mat)
    for i in w:
        new_mat[i[0]][i[1]] = '1'

# 3. 2찾아서 bfs돌리기

    for row in range(N):
        for col in range(M):
            if new_mat[row][col] == '2':
                bfs(new_mat,row,col)
    cnt = 0
    for row in range(N):
        for col in range(M):
            if new_mat[row][col] == '0':
                cnt+=1

    answer.append(cnt)


print(max(answer))

