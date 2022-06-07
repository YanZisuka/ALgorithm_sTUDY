import sys
from collections import deque
input = sys.stdin.readline


d = deque()
n = int(input())

for _ in range(n):
    cmd = input().strip().split()
    if len(cmd) > 1:
        cmd, num = cmd[0], int(cmd[1])
        if cmd == 'push_front': d.appendleft(num)
        elif cmd == 'push_back': d.append(num)
    else:
        cmd = cmd[0]
        if cmd == 'pop_front': print(d.popleft()) if d else print(-1)
        elif cmd == 'pop_back': print(d.pop()) if d else print(-1)
        elif cmd == 'size': print(len(d))
        elif cmd == 'empty': print(1) if not d else print(0)
        elif cmd == 'front': print(d[0]) if d else print(-1)
        elif cmd == 'back': print(d[-1]) if d else print(-1)
        