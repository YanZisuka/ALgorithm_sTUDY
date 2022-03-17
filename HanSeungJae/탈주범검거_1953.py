from collections import deque
import sys
sys.stdin = open('input.txt')

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

"""
위로 볼 때: 1, 2, 5, 6
아래로 볼 때: 1, 2, 4, 7
왼쪽: 1, 3, 4, 5
오른쪽: 1, 3, 6, 7
"""


def setKrange(i, j):
    k_range = []
    if board[i][j] == 1:
        k_range = [0, 1, 2, 3]
    elif board[i][j] == 2:
        k_range = [0, 1]
    elif board[i][j] == 3:
        k_range = [2, 3]
    elif board[i][j] == 4:
        k_range = [0, 3]
    elif board[i][j] == 5:
        k_range = [1, 3]
    elif board[i][j] == 6:
        k_range = [1, 2]
    elif board[i][j] == 7:
        k_range = [0, 2]
    return k_range


def bfs(r, c):
    queue = deque()
    visited[r][c] = True
    queue.append((r, c))
    cnt = 1
    time = 1
    
    while queue:
        moment = len(queue)
        for _ in range(moment):
            if time == l:
                return cnt
            
            i, j = queue.popleft()
            k_range = setKrange(i, j)
            
            for k in k_range:
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < m:
                    if not visited[ni][nj]:
                        if k == 0 and board[ni][nj] in [1, 2, 5, 6]:
                            cnt += 1
                            visited[ni][nj] = True
                            queue.append((ni, nj))
                        elif k == 1 and board[ni][nj] in [1, 2, 4, 7]:
                            cnt += 1
                            visited[ni][nj] = True
                            queue.append((ni, nj))
                        elif k == 2 and board[ni][nj] in [1, 3, 4, 5]:
                            cnt += 1
                            visited[ni][nj] = True
                            queue.append((ni, nj))
                        elif k == 3 and board[ni][nj] in [1, 3, 6, 7]:
                            cnt += 1
                            visited[ni][nj] = True
                            queue.append((ni, nj))
        time += 1
    return cnt


t = int(input())
for tc in range(1, t+1):
    n, m, r, c, l = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    
    print(f'#{tc} {bfs(r, c)}')