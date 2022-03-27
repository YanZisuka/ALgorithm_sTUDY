import sys
input=sys.stdin.readline

N, K = map(int,input().split())
dp = [[0]*(K+1) for _ in range(N+1)]

for n in range(1,N+1):
    W, V = map(int,input().split())
    for k in range(1,K+1):
        if k < W:  # 가방의 용량보다 무게가 더 클 때
            dp[n][k] = dp[n-1][k]  # 안 넣음
        else:
            dp[n][k] = max(dp[n-1][k],dp[n-1][k-W]+V)  # 안 넣거나 vs 기존 물건 빼고 넣기

print(dp[N][K])
