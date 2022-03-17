N = int(input())

memo = [0] * (10 ** 6)
memo[1] = 1
memo[2] = 1
memo[3] = 1


def func(x):
    for i in range(4, x):
        memo[i] = memo[i - 1] + 1
        if i % 3 == 0:
            memo[i] = min(memo[i], memo[i // 3] + 1)
        elif i % 2 == 0:
            memo[i] = min(memo[i], memo[i // 2] + 1)
    return memo[x]


print(func(N))
