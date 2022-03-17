import sys
sys.stdin = open('input.txt')

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def dfs(i, j):
    stack = []
    stack.append((i, j))
    
    while stack:
        i, j = stack.pop()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < 16 and 0 <= nj < 16:
                if maze[ni][nj] == 3:
                    return 1
                if maze[ni][nj] == 0:
                    maze[ni][nj] = 4
                    stack.append((ni, nj))
    return 0


for tc in range(1, 11):
    t = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                print(f'#{tc} {dfs(i, j)}')
