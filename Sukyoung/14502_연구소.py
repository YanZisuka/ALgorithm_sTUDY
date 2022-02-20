from collections import deque
from itertools import combinations
from copy import deepcopy

def bfs(map,start_x,start_y):
    queue = deque()  # 탐색할 리스트
    queue.append([start_x,start_y])  # 탐색할 리스트에 시작 좌표 추가

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if map[nx][ny] == '0':  # 안전구역인 경우,
                    queue.append([nx,ny])  # 방문(탐색)할 리스트에 추가하고
                    map[nx][ny] = '2'  # 감염


# 1. 입력 받기

N, M = list(map(int,input().split()))
map = [input().split() for _ in range (N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 2. 벽을 세울 수 있는 좌표(0인 좌표)들 구하기

pre_wall = []
for row in range(N):
    for col in range(M):
        if map[row][col] == '0':
            pre_wall.append([row,col])

# 3. 벽 세우기

wall_list = list(combinations(pre_wall,3))  # 조합으로 벽 3개 세우는 모든 경우 구하기
count_list=[]
for walls in wall_list:
    test_map = deepcopy(map) # 깊은 복사로 text_map 만들기
    for wall in walls:
        test_map[wall[0]][wall[1]] = '1'

    # 4. dfs 함수 시작 좌표 (2인 좌표) 구하고 dfs 함수에 넣기

    two_list=[]
    for row in range(N):
        for col in range(M):
            if test_map[row][col] == '2':
                two_list.append([row,col])
    for start in two_list:
        bfs(test_map,start[0],start[1])

    # 5. 결과 map에서 안전구역(0인 좌표) 수의 최대값 구하기

    count=0
    for row in range(N):
        for col in range(M):
            if test_map[row][col]=='0':
                count += 1
    count_list.append(count)
print(max(count_list))




