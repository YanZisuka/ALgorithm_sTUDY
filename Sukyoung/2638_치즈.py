from collections import deque

def bfs(start_x,start_y,now):
    queue = deque()
    queue.append([start_x,start_y])
    grid[start_x][start_y] -= 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if grid[nx][ny] == now:
                    queue.append([nx,ny])
                    grid[nx][ny] -= 1
                elif grid[nx][ny] >= 1:
                    grid[nx][ny]+=1


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


i = 0
while cheese(grid):
    bfs(0,0,i)

    for row in range(N):
        for col in range(M):
            if grid[row][col] >= 3:
                grid[row][col] = i-1
            elif grid[row][col] == 2:
                grid[row][col] = 1
            elif grid[row][col] == 1:
                grid[row][col] = 1
            elif grid[row][col] != i-1:
                grid[row][col] = i-1
    i -= 1


print(-i)




