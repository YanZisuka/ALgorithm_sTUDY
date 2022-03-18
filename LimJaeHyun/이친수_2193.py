import sys
input = sys.stdin.readline
memo = [0] * 92


def fibo(n):
    memo[1] = 1
    memo[2] = 1
    for idx in range(3, n + 1):
        memo[idx] = memo[idx - 1] + memo[idx - 2]
    return memo[n]


print(fibo(int(input())))
