import sys
sys.stdin = open('input.txt')


def set_start_and_goal():
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                start = (i, j)
            elif maze[i][j] == 3:
                goal = (i, j)
    
    return start, goal


def dfs(a, b):
    visited[a][b] = True
    stack = []
    stack.append((a, b))
    
    while stack:
        i, j = stack.pop()
        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if maze[ni][nj] != 1 and not visited[ni][nj]:
                    visited[ni][nj] = True
                    stack.append((ni, nj))
                    
    if visited[goal[0]][goal[1]]:
        return 1
    else:
        return 0


def dfs_recursive(i, j):
    visited[i][j] = True

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < n:
            if maze[ni][nj] != 1 and not visited[ni][nj]:
                dfs_recursive(ni, nj)
    
    if visited[goal[0]][goal[1]]:
        return 1
    else:
        return 0


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    
    try:
        start, goal = set_start_and_goal()
        print(f'#{tc} {dfs_recursive(*start)}')
    except UnboundLocalError:
        print(f'#{tc} error')