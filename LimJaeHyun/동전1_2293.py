import sys
input = sys.stdin.readline

n, k = map(int, input().split())
memo = [0] * (k + 2)
coin_list = list(int(input()) for _ in range(n))
memo[0] = 1
for coin in coin_list:
    for i in range(coin, k + 1):
        memo[i] += memo[i - coin]

print(memo[k])


