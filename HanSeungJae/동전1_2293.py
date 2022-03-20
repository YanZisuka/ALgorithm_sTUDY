import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0] * (k+1)

for i in range(n):
    coin = int(input())

    for j in range(k+1):
        if j == coin:
            dp[j] += 1
        else:
            if j - coin >= 0:
                dp[j] = dp[j] + dp[j-coin]

print(dp[k])