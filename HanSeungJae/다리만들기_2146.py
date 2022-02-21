from collections import deque


def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 2
    cnt = 1

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if cnt > 2 and graph[ni][nj] == 1:
                    return cnt
                if graph[ni][nj] == 0:
                    graph[ni][nj] = 2
                    queue.append((ni, nj))
                    cnt += 1
    return cnt


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
cnts = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            cnts.append(bfs(graph, i, j))

print(cnts)