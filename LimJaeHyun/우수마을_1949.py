import sys
sys.setrecursionlimit(100000000)

N = int(input())
villages = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
memo = [[0, 0] for _ in range(N + 1)]
populations = [0] + list(map(int, input().split()))
for _ in range(N - 1):
    town1, town2 = map(int, input().split())
    villages[town1].append(town2)
    villages[town2].append(town1)


def dfs(node):
    visited[node] = True
    memo[node][0] = 0
    memo[node][1] += populations[node]

    for i in villages[node]:
        if not visited[i]:
            dfs(i)
            memo[node][0] += max(memo[i][1], memo[i][0]) # 문제 조건을 잘 읽기, 사회망서비스와는 다르다.
            memo[node][1] += memo[i][0] # 윗줄: 어쩌면 우수마을이 아닌 마을끼리 붙어버리는거 아닐까


dfs(1)
print(max(memo[1][0], memo[1][1]))
