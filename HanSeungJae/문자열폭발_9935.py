import sys
input = sys.stdin.readline

st = input().strip()
bomb = input().strip()
n = len(st)
m = len(bomb)
stack = []

for i in range(n):
    stack.append(st[i])

    if len(stack) >= m:
        if ''.join(stack[-m:]) == bomb:
            for _ in range(m):
                stack.pop()

ans = ''.join(stack)

if ans:
    print(ans)
else:
    print('FRULA')