N = int(input())
social_network = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(N):
    node1, node2 = map(int, input().split())
    social_network[node1].append(node2)
    social_network[node2].append(node1)

memo = [[0, 0] for _ in range(N + 1)]


def dfs(node):
    visited[node] = True
    memo[node][0] = 0
    memo[node][1] = 1

    for i in social_network[node]:
        if not visited[i]:
            dfs(i)
            memo[node][0] += memo[i][1]
            memo[node][1] += min(memo[i][0], memo[i][1])


dfs(1)
print(min(memo[1][0], memo[1][1]))
