import sys
from collections import deque

d_row = [1, -1, 0, 0]
d_col = [0, 0, 1, -1]

def bfs(now_pos, now_size):

    dq = deque()
    dq.append(now_pos)
    visit[now_pos[0]][now_pos[1]] = 1
    while dq:
        row, col = dq.popleft()
        for d in range(4):
            n_row = d_row[d] + row
            n_col = d_col[d] + col
            if n_row < 0 or n_col < 0 or n_row >= N or n_col >= N:
                continue
            if visit[n_row][n_col] != 0:
                continue
            if graph[n_row][n_col] > now_size:
                continue
            visit[n_row][n_col] = visit[row][col] + 1
            dq.append((n_row, n_col))

def get_min_dist(now_size):

    row, col = 0, 0
    min_dist = int(1e9)
    for i in range(N):
        for j in range(N):
            if visit[i][j] != 0 and graph[i][j] > 0 and graph[i][j] < now_size:
                if min_dist > visit[i][j] - 1:
                    min_dist = visit[i][j] - 1
                    row = i
                    col = j
    return (row, col, min_dist)

N = int(sys.input())
graph = [[] for _ in range(N)]

answer = 0
now_size = 2
now_ate = 0
now_pos = (0, 0)
for i in range(N):
    arr = list(map(int, input().split()))
    now = [(i, j) for j, a in enumerate(arr) if a == 9]
    if now: now_pos = now[0]
    graph[i] = arr
graph[now_pos[0]][now_pos[1]] = 0


print(answer)