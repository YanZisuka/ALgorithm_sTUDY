import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

memo = [1] * N

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            memo[i] = max(memo[i], memo[j] + 1)

print(max(memo))
