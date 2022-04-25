import sys
input = sys.stdin.readline


def dfs(now):
    cnt = 0

    stack = []
    stack.append(now)
    visited[now] = True

    while stack:
        now = stack.pop()

        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)
                cnt += 1
    return cnt


n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
m = int(input())

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

answer = dfs(1)

print(answer)