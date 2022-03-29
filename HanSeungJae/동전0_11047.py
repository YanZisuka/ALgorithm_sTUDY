import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
cnt = 0

for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

for i in range(n):
    if coins[i] <= k:
        cnt += k // coins[i]
        k -= coins[i] * (k // coins[i])

        if k == 0:
            break

print(cnt)