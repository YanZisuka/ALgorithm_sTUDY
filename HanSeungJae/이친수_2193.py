import sys
input = sys.stdin.readline


def fib():
    for i in range(n + 1):
        if len(memo) <= i:
            memo.append(memo[i - 1] + memo[i - 2])


n = int(input())
memo = [0, 1]

fib()
        
print(memo[n])