import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def dfs(now):
    visited[now] = True
    dp[1][now] = residentNum[now]

    for nxt in tree[now]:
        if not visited[nxt]:
            dfs(nxt)
            dp[0][now] += max(dp[0][nxt], dp[1][nxt])
            dp[1][now] += dp[0][nxt]


n = int(input())
residentNum = [0] + list(map(int, input().split()))
tree = [[] for _ in range(n+1)]
visited = [False] * (n+1)
dp = [[0] * (n+1) for _ in range(2)]  # dp[0]: i번째가 우수 마을이 아님, dp[1]: i번째가 우수마을

for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dfs(1)

print(max(dp[0][1], dp[1][1]))