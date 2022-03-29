import sys
sys.stdin = open('input.txt')


def dfs(step, i, j, score):
    global ans
    if step == n-1:
        ans = min(ans, score)
        return
    
    ni = j
    for nj in dj:
        if not visited[nj] and step != n-2 and nj != 0:
            visited[nj] = True
            dfs(step + 1, ni, nj, score + board[ni][nj])
            visited[nj] = False
        elif not visited[nj] and step == n-2 and nj == 0:
            visited[nj] = True
            dfs(step + 1, ni, nj, score + board[ni][nj])
            visited[nj] = False


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    dj = [i for i in range(n)]
    ans = float('inf')
    
    for j in range(1, n):
        visited[j] = True
        dfs(0, 0, j, board[0][j])
        visited[j] = False

    print(f'#{tc} {ans}')