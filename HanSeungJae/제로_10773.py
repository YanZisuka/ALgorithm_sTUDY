import sys
input = sys.stdin.readline

k = int(input())
stack = []

for _ in range(k):
    st = int(input())
    if st == 0:
        stack.pop()
    else:
        stack.append(st)

print(sum(stack))