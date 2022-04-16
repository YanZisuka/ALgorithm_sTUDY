import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * (n+1)
answer = []

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

maxVal = max(dp)

for i in range(n-1, -1, -1):
    if dp[i] == maxVal:
        answer.append(arr[i])
        maxVal -= 1

print(max(dp))
print(*answer[::-1])