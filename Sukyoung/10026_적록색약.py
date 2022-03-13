from collections import deque

def no_bfs(s_row,s_col,num,color): # 적록색약 아닌 사람 bfs
    queue = deque()
    queue.append([s_row,s_col])
    mat[s_row][s_col] = num # 방문 처리 - num으로 바꿈
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0 <= ny < N and mat[nx][ny]==color: # color에 해당되면 지정된 num으로 바꿔줌
                queue.append([nx,ny])
                mat[nx][ny] = num
                cnt += 1

    return cnt

def yes_bfs(s_row,s_col,min,max):  # 적록색약인 사람 bfs
    queue = deque()
    queue.append([s_row,s_col])
    mat[s_row][s_col] = 0 # 방문 처리 0으로
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0 <= ny < N and min <= mat[nx][ny] <= max: # 해당 범위 만족하면 0으로 바꾸기
                queue.append([nx,ny])
                mat[nx][ny] = 0
                cnt += 1

    return cnt

N = int(input())
mat = [list(input()) for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

no = []
for row in range(N):  # 색마다 숫자 지정
    for col in range(N):
        if mat[row][col] == 'R':
            no.append(no_bfs(row,col,3,'R'))
        elif mat[row][col] == 'G':
            no.append(no_bfs(row,col,2,'G'))
        elif mat[row][col] == 'B':
            no.append(no_bfs(row,col,1,'B'))

yes=[]
for row in range(N):
    for col in range(N):
        if mat[row][col] >= 2:  # R=3,G=2 이므로 2 이상이면 적록
            yes.append(yes_bfs(row,col,2,3))
        elif mat[row][col] == 1: # 1은 파랑
            yes.append(yes_bfs(row, col,1,1))

print(len(no),len(yes))