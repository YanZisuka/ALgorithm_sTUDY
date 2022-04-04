from collections import deque
import sys
sys.stdin = open('input.txt')

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(si, sj, ei, ej):
    q = deque()
    visited = [[float('inf')] * n for _ in range(n)]
    q.append((si, sj))
    visited[si][sj] = arr[si][sj]
    
    while q:
        ci, cj = q.popleft()
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if visited[ni][nj] > visited[ci][cj] + arr[ni][nj]:
                    visited[ni][nj] = visited[ci][cj] + arr[ni][nj]
                    q.append((ni, nj))
    
    return visited[ei][ej]        
    
        
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    ans = bfs(0, 0, n-1, n-1)
    
    print(f'#{tc} {ans}')