import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def dfs(now):
    visited[now] = True
    dp[1][now] = 1
    
    for nxt in tree[now]:
        if not visited[nxt]:
            dfs(nxt)
            dp[1][now] += min(dp[1][nxt], dp[0][nxt])
            dp[0][now] += dp[1][nxt]


n = int(input())
tree = [[] for _ in range(n+1)]
visited = [False] * (n+1)
dp = [[0] * (n+1) for _ in range(2)]  # dp[0]: i번째 노드가 얼리 어답터가 아닌 경우, dp[1]: 얼리 어답터인 경우

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1)

print(min(dp[0][1], dp[1][1]))
