import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(x):
    visited[x]=1
    for i in friends[x]:
        if visited[i] == 0:
            dfs(i)

            dp[x][0] += min(dp[i][0],dp[i][1]) # x가 얼리어답터인 경우 - 자식은 min(얼리어답터O,얼리어답터x)
            dp[x][1] += dp[i][0]  # x가 얼리어답터 아닌 경우 - 자식은 무조건 얼리어답터


N = int(input())
friends = [[] for _ in range(N+1)]
dp = [[1,0] for _ in range(N+1)] # [얼리어답터인 경우,얼리어답터 아닌 경우]
visited = [0]*(N+1)
for i in range(N-1):
    u,v = map(int,input().split())
    friends[u].append(v)
    friends[v].append(u)


dfs(1)
print(min(dp[1][0],dp[1][1]))

# 트리를 양방향으로 입력 받아야 통과가 되는데 왜 꼭 그렇게 해야하는지 모르겠다ㅠ