def dfs(x, y,cnt):
    global max_cnt
    visited[ord(mat[x][y])-65] = True
    if cnt > max_cnt: # 가장 많이 재귀가 돌았을 때의 값 찾기
        max_cnt = cnt

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C:
            if not visited[ord(mat[nx][ny])-65]:
                dfs(nx,ny,cnt+1) # cnt는 재귀가 돌아간 횟수,
                visited[ord(mat[nx][ny]) - 65] = False # 재귀가 끝나면 그 전단계로

R, C = map(int,input().split())
mat = [list(input()) for _ in range(R)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [False]*26
cnt = 1
max_cnt = 1
dfs(0,0,cnt)
print(max_cnt)


# 근데 word에 append해서 not in 검사하는거랑 false 26개 만드는거랑 시간에서 어떤 차이가 나는걸까.....



