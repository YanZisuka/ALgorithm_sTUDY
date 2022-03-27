import sys
input = sys.stdin.readline

st1 = input().strip()
st2 = input().strip()

n1 = len(st1)
n2 = len(st2)

dp = [[0] * (n2+1) for _ in range(n1+1)]

for i in range(1, n1+1):
    for j in range(1, n2+1):
        if st1[i-1] == st2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n1][n2])