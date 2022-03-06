import sys
sys.setrecursionlimit(100000)

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def dfs(i, j, cnt):
    visited[ord(board[i][j])-65] = True

    global ans
    ans = max(ans, cnt)

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < r and 0 <= nj < c:
            if not visited[ord(board[ni][nj])-65]:
                dfs(ni, nj, cnt+1)
                visited[ord(board[ni][nj])-65] = False


r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
visited = [False] * 26

ans = 1
dfs(0, 0, ans)
print(ans)