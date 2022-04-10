import sys
from collections import deque
input = sys.stdin.readline


def topologySort():
    q = deque()

    for i in range(1, n+1):
        if inDegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for nxt, partsNum in graph[now]:
            if dp[now].count(0) == n+1:
                dp[nxt][now] += partsNum
            else:
                for i in range(1, n+1):
                    dp[nxt][i] += dp[now][i] * partsNum
            inDegree[nxt] -= 1
            if inDegree[nxt] == 0:
                q.append(nxt)


n = int(input())
graph = [[] for _ in range(n+1)]
inDegree = [0] * (n+1)
dp = [[0] * (n+1) for _ in range(n+1)]

m = int(input())
for i in range(m):
    x, y, k = map(int, input().split())
    graph[y].append((x, k))
    inDegree[x] += 1

topologySort()

for idx, partsNum in enumerate(dp[n]):
    if partsNum > 0:
        print(idx, partsNum)
