import sys

input = lambda: sys.stdin.readline().strip()
LIMIT = 1000000

n = int(input())
fs = {i: 0 for i in range(1, LIMIT + 1)}
arr = list(map(int, input().split()))
for el in arr:
    fs[el] += 1

ans = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and fs[arr[stack[-1]]] < fs[arr[i]]:
        ans[stack.pop()] = arr[i]
    stack.append(i)

print(*ans)
