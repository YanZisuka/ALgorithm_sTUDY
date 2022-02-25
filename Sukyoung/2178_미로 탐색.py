from collections import deque

def bfs(end_x, end_y):
    queue = deque()  # 방문 예정 리스트
    queue.append([0,0])  # 시작 노드 [0,0]
    maze[0][0] = '0'  # 방문 처리
    count = [[0]*M for _ in range(N)]  # 카운트 할 matrix

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:  # 범위를 만족하고
                if maze[nx][ny] == '1':  # 이동 가능 하면,
                    queue.append([nx,ny])  # 방문 예정 리스트 추가
                    maze[nx][ny] = '0'    # 방문처리
                    count[nx][ny] = count[x][y] + 1  # 시작점으로 부터 이동 거리 카운트
                    if nx == end_x-1 and ny == end_y-1:  # 도착하면, 카운트한 이동 거리 반환
                        return count[nx][ny]


N, M = map(int,input().split())
maze = [list(input()) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

print(bfs(N,M)+1) # 시작 위치 포함해서 거리 반환
