import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = [0] * (n+1)
prefixSum = [0] * (n+1)
dp = [0] * (n+1)

for i in range(1, n+1):
    arr[i] = int(input())
    prefixSum[i] = prefixSum[i-1] + arr[i]

dp[m] = prefixSum[m]
for i in range(m+1, n+1):
    dp[i] = max(dp[i-1] + arr[i], prefixSum[i] - prefixSum[i-m])

print(max(dp))