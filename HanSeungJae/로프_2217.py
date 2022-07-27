import sys
input = lambda: sys.stdin.readline().strip()


n = int(input())
arr = []
answer = 0

for _ in range(n):
    arr.append(int(input()))

arr.sort()

for i in range(n - 1, -1, -1):
    arr[i] = arr[i] * (n - i)
    answer = max(answer, arr[i])

print(answer)