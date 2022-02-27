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
                    queue.append([nx, ny])  # 방문 예정 리스트 추가
                    visited[nx][ny] = 1  # 방문처리
                    count[nx][ny] = count[x][y] + 1  # 시작점으로 부터 이동 거리 카운트
                    if mat[nx][ny] < baby and mat[nx][ny] != 0: # 도착하면, 카운트한 이동 거리 반환
                        eat.append([nx,ny,count[nx][ny]])

    return eat

N = int(input())
mat = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

result = 0
baby = 2
fish = 0
fishlist = []

def find(mat):
    global row
    global col
    for row in range(N):
        for col in range(N):
            if mat[row][col] == 9:
                return row,col

while 1:
    find(mat)
    bfs(row,col,baby)
    min_eat = sorted(eat,key=lambda x:(x[2],x[0],x[1]))
    if eat:
        mat[min_eat[0][0]][min_eat[0][1]] = 9
        mat[row][col] = 0
        fish += 1
        result += min_eat[0][2]
        if baby == fish:
            baby+=1
            fish = 0
    else:
        break

fishlist =[]

print(result)