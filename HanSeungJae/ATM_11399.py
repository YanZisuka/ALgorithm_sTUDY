import sys
input = lambda: sys.stdin.readline().strip()


n = int(input())
arr = list(map(int, input().split()))

arr.sort()
for i in range(1, n):
    arr[i] += arr[i-1]

answer = sum(arr)

print(answer)