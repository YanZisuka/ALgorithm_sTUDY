import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)  # 이거 없으면 런타임에러ㅠ

def dfs(x,y):
    if eat[x][y] != 0:
        return eat[x][y]
    eat[x][y] = 1

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n and forest[x][y] < forest[nx][ny]:
            eat[x][y] = max(eat[x][y],dfs(nx,ny)+1)
    return eat[x][y]

n = int(input())
forest = [list(map(int,input().split())) for _ in range(n)]
eat = [[0]*n for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

max_cnt = 0
for row in range(n):
    for col in range(n):
        max_cnt = max(max_cnt,dfs(row,col))
print(max_cnt)

