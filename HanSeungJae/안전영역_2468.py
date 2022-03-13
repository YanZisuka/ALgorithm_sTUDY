import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def dfs(i, j, height):

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < n:
            if not visited[ni][nj] and graph[ni][nj] > height:
                visited[ni][nj] = True
                dfs(ni, nj, height)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

max_height = max(map(max, graph))
safety_zones = 0

for k in range(max_height+1):
    cnt = 0
    visited = [[False] * n for _ in range(n)]
        
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > k:
                visited[i][j] = True
                dfs(i, j, k)
                cnt += 1
    
    safety_zones = max(safety_zones, cnt)

print(safety_zones)