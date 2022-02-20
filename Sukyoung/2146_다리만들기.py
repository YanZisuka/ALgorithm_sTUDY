from collections import deque
from copy import deepcopy

# bfs 함수 1 - 섬마다 각각 다른 숫자를 넘버링 하는 함수
def bfs_numbering(map,start_x,start_y,number):
    queue = deque()
    queue.append([start_x,start_y])
    map[start_x][start_y] = number

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if map[nx][ny] == 1:
                    queue.append([nx,ny])
                    map[nx][ny] = number

# bfs 함수 2 - 최단 거리를 탐색하는 함수
def bfs_bridge(map,start_x,start_y):
    queue = deque()
    queue.append([start_x,start_y])
    count_matrix = [[0]*N for _ in range(N)] # 최단 경로 출력을 위한 matrix

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if map[nx][ny] == 0:  # 바다인 경우 (0인 좌표)
                    queue.append([nx, ny])
                    map[nx][ny] = 1
                    count_matrix[nx][ny] = count_matrix[x][y]+1  # 시작 좌표에서 얼마나 이동했는지
                elif map[nx][ny] > num:  # 다른 섬을 만났을 경우 (자기보다 큰 수 가진 좌표)
                    count_matrix[nx][ny] = count_matrix[x][y] + 1
                    return count_matrix[nx][ny]
    return 200

# 1. 입력 받기

N =int(input())
map = [list(map(int,input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 2. 넘버링 dfs의 시작 좌표 설정, 함수 실행

number = 1  # 넘버링할 숫자
for row in range(N):
    for col in range(N):
        if map[row][col] == 1:
            number += 1  # 2,3,4.....로 넘버링
            bfs_numbering(map,row,col,number)


# 3. 최단 경로를 찾을 시작 좌표 설정, 함수 실행

count_list = []
for num in range(2,number):
    for row in range(N):
        for col in range(N):
            if map[row][col] == num:
                test_map = deepcopy(map)
                count_list.append(bfs_bridge(test_map,row,col))

print(min(count_list)-1)  # 최단 경로