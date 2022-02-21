from collections import deque


def bfs(board, a, b):
    queue = deque()
    queue.append((a, b))
    
    while queue:
        i, j = queue.popleft()
        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m:
                if board[ni][nj] == 1:
                    board[ni][nj] = board[i][j] + 1
                    queue.append((ni, nj))
    return board[n-1][m-1]
          

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
    
print(f'{bfs(board, 0, 0)}')