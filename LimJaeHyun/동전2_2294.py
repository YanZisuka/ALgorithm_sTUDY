import sys
input = sys.stdin.readline

memo = [float('inf')] * 1000002
n, k = map(int, input().split())
memo[0] = 0
coin_list = [int(input()) for _ in range(n)]
for coin in coin_list:
    for i in range(coin, k + 1):
        memo[i] = min(memo[i - coin] + 1, memo[i])

print(memo[k])

# coin_list = list(set(list(int(input()) for _ in range(n))))
# coin_list.sort()
# coin_count = 0
# for idx in range(len(coin_list) - 1, -1, -1):
#     if coin_list[idx] == 1:
#         coin_count += k
#         continue
#     while k % coin_list[idx] == 0 and k != 0:
#         coin_count += k // coin_list[idx]
#         k = k % coin_list[idx]
# if coin_count == 0:
#     print(-1)
# else:
#     print(coin_count)
