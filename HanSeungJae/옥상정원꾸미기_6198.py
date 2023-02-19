import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
buildings = [None]
for _ in range(n):
    buildings.append(int(input()))

ans = 0
stack = []
for i in range(1, n + 1):
    while stack and stack[-1] <= buildings[i]:
        stack.pop()

    stack.append(buildings[i])
    ans += len(stack) - 1

print(ans)
