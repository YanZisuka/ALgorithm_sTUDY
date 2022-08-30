import sys
input = lambda: sys.stdin.readline().strip()


def check(st: str) -> bool:
    stack = []
    for char in st:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                return False
    if stack: return False
    return True


t = int(input())
for _ in range(t):
    res = check(input())
    if res: print('YES')
    else: print('NO')
    