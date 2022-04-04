import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
height = 0
ans = float('inf')
for i in range(257):
    pop = 0
    build = 0
    for j in range(n):
        for k in range(m):
            if board[j][k] < i:
                build += (i - board[j][k])
            else:
                pop += (board[j][k] - i)
    inven = pop + b
    if inven < build:
        continue
    time = 2 * pop + build
    if ans >= time:
        ans = time
        height = i

print(ans, height)
