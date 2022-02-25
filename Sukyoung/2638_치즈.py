from collections import deque

def bfs(start_x,start_y,now):
    queue = deque()
    queue.append([start_x,start_y])
    grid[start_x][start_y] -= 1 # 방문처리 -1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if grid[nx][ny] == now:
                    queue.append([nx,ny])
                    grid[nx][ny] -= 1
                elif grid[nx][ny] >= 1: # 치즈를 만나면 +1
                    grid[nx][ny]+=1


# 치즈가 남아있는지 판별하는 함수
def cheese(grid):
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                return True
    return False


N, M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


i = 0 # 현재 갈 수 있는 길
while cheese(grid): # 치즈가 있으면 실행
    bfs(0,0,i)

    for row in range(N):
        for col in range(M):
            if grid[row][col] >= 3:  # 두 번 만난 치즈는 사라짐 (그냥 길로 바뀜)
                grid[row][col] = i-1
            elif grid[row][col] == 2:  # 한 번 만난 치즈는 다시 새 치즈(1)로 바꿔줌
                grid[row][col] = 1
            elif grid[row][col] == 1:  # 한 번도 안마주친 치즈도 그대로 새 치즈
                grid[row][col] = 1
            elif grid[row][col] != i-1:  # 나머지는 다 그냥 길로 바뀜
                grid[row][col] = i-1
    i -= 1  # while문이 반복되는 횟수 = 치즈 다 녹는 시간

print(-i)




