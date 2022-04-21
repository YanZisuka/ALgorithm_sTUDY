import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def dfs(now):
    visited[now] = True
    dp[now] = 1

    for nxt in tree[now]:
        if not visited[nxt]:
            dfs(nxt)
            dp[now] += dp[nxt]


n, r, q = map(int, input().split())
tree = [[] for _ in range(n+1)]
visited = [False] * (n+1)
dp = [0] * (n+1)

for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dfs(r)

for _ in range(q):
    print(dp[int(input())])