import sys
from collections import deque
input = sys.stdin.readline


def bfs(a, cnt):
    q = deque()
    q.append((a, cnt))

    while q:
        now, cnt = q.popleft()
        if now == b:
            return cnt

        if now * 2 <= b:
            q.append((now * 2, cnt+1))

        if now * 10 + 1 <= b:
            q.append((now * 10 + 1, cnt+1))
    return -1
    

a, b = map(int, input().split())

answer = bfs(a, 0)

if answer != -1:
    print(answer+1)
else:
    print(answer)