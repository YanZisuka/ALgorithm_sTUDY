import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == 1 and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni, nj))


t = int(input())
for tc in range(1, t+1):
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    answer = 0

    for _ in range(k):
        a, b = map(int, input().split())
        board[b][a] = 1

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                answer += 1

    print(answer)
