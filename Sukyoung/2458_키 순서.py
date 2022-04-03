import sys
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [[1000]*(N+1) for _ in range(N+1)]
for i in range(M):
    row,col = map(int,input().split())
    graph[row][col] = 1
for i in range(N+1):
    graph[i][i] = 0

for i in range(1,N+1):
    for row in range(1,N+1):
        for col in range(1,N+1):
            graph[row][col] = min(graph[row][col],graph[row][i]+graph[i][col])

count = [0]*(N+1)
for row in range(1,N+1):
    for col in range(1,N+1):
        if graph[row][col] < 1000 or graph[col][row] < 1000:
            count[row] += 1


print(count.count(N))