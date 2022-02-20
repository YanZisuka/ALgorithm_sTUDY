from collections import deque

def bfs(map ,start_x,start_y):
    queue = deque() # 방문 예정 리스트
    queue.append([start_x,start_y]) # 방문 예정 리스트에 시작 좌표 추가
    map[start_x][start_y] = '0' # 방문 처리
    count = 1

    while queue:
        x,y = queue.popleft() # 먼저 추가 된 것부터 꺼내기(queue)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:  # x,y가 map의 범위를 넘어가지 않고,
                if map[nx][ny] == '1':  # x,y 좌표가 1이면,
                    queue.append([nx,ny]) # 방문 예정 리스트에 추가
                    map[nx][ny] = '0'  # 방문 처리
                    count += 1

    return count

# 1. 입력 받기

N = int(input())
map = [list(input()) for _ in range (N)]


dx = [1, 0, -1, 0]  # bfs에서 탐색할 좌표들 (우>하>좌>상)
dy = [0, -1, 0, 1]

# 2. map에서 1인 좌표 찾기 (dfs 시작 죄표 찾기) -> bfs 함수에 넣어주기

count_list = []
for row in range(N):
    for col in range(N):
        if map[row][col] == '1':
            count_list.append(bfs(map,row,col))


# 3. count 리스트 정렬해서 출력

count_list.sort()
number = len(count_list)
print(number)
for num in count_list:
    print(num)






