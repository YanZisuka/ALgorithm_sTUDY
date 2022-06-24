import sys
input = sys.stdin.readline


def floyd():
    for md in range(n):
        for st in range(n):
            for en in range(n):
                if graph[st][en] > graph[st][md] + graph[md][en]:
                    graph[st][en] = graph[st][md] + graph[md][en]
                
    
INF = float('inf')
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = INF

floyd()

for i in range(n):
    for j in range(n):
        print(1, end=' ') if graph[i][j] < INF else print(0, end=' ')
    print()