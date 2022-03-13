from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def BFS(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    cnt = 1

    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if graph[ni][nj] == 1:
                    graph[ni][nj] = 0
                    queue.append((ni, nj))
                    cnt += 1
    return cnt


def dfs(graph, a, b):
    stack = []
    stack.append((a, b))
    graph[a][b] = 0
    cnt = 1
    
    while stack:
        i, j = stack.pop()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if graph[ni][nj] == 1:
                    graph[ni][nj] = 0
                    stack.append((ni, nj))
                    cnt += 1
    return cnt


n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

complex_list = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            complex_list.append(dfs(graph, i, j))

complex_list.sort()
print(len(complex_list))
for i in range(len(complex_list)):
    print(complex_list[i])