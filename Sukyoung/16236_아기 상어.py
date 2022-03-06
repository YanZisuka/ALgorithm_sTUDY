from collections import deque

def bfs(start_x,start_y,baby):
    global fish
    global eat
    queue = deque()
    queue.append([start_x,start_y])
    visited = [[0] * N for _ in range(N)]
    visited[start_x][start_y] = 1
    mat[start_x][start_y] = 0
    count = [[0]*N for _ in range(N)]
    eat = []

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if mat[nx][ny] <= baby and visited[nx][ny] == 0:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1  # 방문처리
                    count[nx][ny] = count[x][y] + 1  # 시작점으로 부터 이동 거리 카운트
                    if mat[nx][ny] < baby and mat[nx][ny] != 0:
                        eat.append([nx,ny,count[nx][ny]]) # 먹을 수 있는 물고기 위치, 거리 모두 리스트에 추가

    return eat

N = int(input())
mat = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

result = 0
baby = 2  # 현재 상어 크기
fish = 0  # 지금까지 먹은 물고기 수

def find(mat):  # 상어 현재 위치 찾는 함수
    global row
    global col
    for row in range(N):
        for col in range(N):
            if mat[row][col] == 9:
                return row,col

while 1:
    find(mat)
    bfs(row,col,baby)
    min_eat = sorted(eat,key=lambda x:(x[2],x[0],x[1])) # 가까운순, 가장 위쪽, 가장 왼쪽 순서로 정렬
    if eat:  # 먹을 수 있는 물고기가 있으면
        mat[min_eat[0][0]][min_eat[0][1]] = 9  # 정렬 결과 중 가장 앞의 물고기 먹고 이동
        mat[row][col] = 0  # 원래 상어가 있던 자리는 0
        fish += 1  # 지금까지 먹은 물고기 +1
        result += min_eat[0][2]  # 지금까지 이동한 거리 (=시간)
        if baby == fish:  # 자기 크기만큼 먹으면, 자기 크기 +1
            baby+=1
            fish = 0
    else:  # 먹을 수 있는 물고기 없으면 끝
        break

print(result)