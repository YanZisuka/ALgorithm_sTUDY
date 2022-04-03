import sys
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [[1000]*(N+1) for _ in range(N+1)]  # 초기값 1000으로 설정
for i in range(M):
    row,col = map(int,input().split())
    graph[row][col] = 1  # 노드가 연결되어 있으면 1
for i in range(N+1):
    graph[i][i] = 0  # 대각선(자기자신) 0

for i in range(1,N+1):  # 순회하면서 특정 노드를 통해 연결되는 경우 (키 비교가 가능한 경우) 찾아줌
    for row in range(1,N+1):
        for col in range(1,N+1):
            graph[row][col] = min(graph[row][col],graph[row][i]+graph[i][col])

# 연결되지 않은 노드는 1000으로 설정되어 있으므로 각 열과 행에서 1000 이하의 수 count
count = [0]*(N+1)
for row in range(1,N+1):
    for col in range(1,N+1):
        if graph[row][col] < 1000 or graph[col][row] < 1000:
            count[row] += 1


print(count.count(N))