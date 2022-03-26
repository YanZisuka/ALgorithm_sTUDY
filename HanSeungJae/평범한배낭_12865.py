import sys
input = sys.stdin.readline

# def knapsack(n, k, w, v):
#     if n <= 0 or k <= 0:
#         return 0
#     if w[n] > k:
#         val = knapsack(n-1, k, w, v)
#         # print(n-1, k, val)
#         return val
#     else:
#         left = knapsack(n-1, k, w, v)
#         # print(n-1, k, left)
#         right = knapsack(n-1, k-w[n], w, v)
#         # print(n-1, k-w[n], right)
#         return max(left, v[n] + right)


n, k = map(int, input().split())
dp = [[0] * (k+1) for _ in range(n+1)]
objects = [[0, 0]]

for i in range(1, n+1):
    objects.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = objects[i][0]
        v = objects[i][1]

        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)    

print(dp[n][k])
