from collections import deque
import copy

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def numbering_bfs(a, b):
    global island_num
    queue = deque()
    queue.append((a, b))

    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if graph[ni][nj] == 1:
                    queue.append((ni, nj))
                    graph[ni][nj] = island_num
    return


def distance_bfs(a, b):
    global min_dist
    queue = deque()
    queue.append((a, b))
    visited = copy.deepcopy(visited_origin)
    visited[a][b] = True
    dist[a][b] = 1

    while queue:
        i, j = queue.popleft()
        if dist[i][j] >= min_dist:
            return

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if not visited[ni][nj] and graph[ni][nj] == 0:
                    queue.append((ni, nj))
                    visited[ni][nj] = True
                    dist[ni][nj] = dist[i][j] + 1
                if graph[ni][nj] != 0 and graph[ni][nj] != island:
                    if dist[i][j] < min_dist:
                        min_dist = dist[i][j]
                    return
    return


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dist = [[0] * n for _ in range(n)]
visited_origin = [[False] * n for _ in range(n)]
island_num = 2
min_dist = float('inf')

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            numbering_bfs(i, j)
            island_num += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < n:
                    if graph[ni][nj] > 1:
                        island = graph[ni][nj]
                        distance_bfs(i, j)
                        break


print(min_dist)