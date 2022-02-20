import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in (1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    danji = []
    cnt = 0
    d_row = [-1, 1, 0, 0]
    d_col = [0, 0, -1, 1]  # 상하좌우 움직임


    def dfs(row, col):
        global cnt
        if row < 0 or row >= N or col < 0 or col >= N:
            return False
        if matrix[row][col] == 1:
            cnt += 1
            matrix[row][col] = 0
            for i in range(4):
                dfs(row + d_row[i], col + d_col[i])
            return True


    for i in range(N):
        for j in range(N):
            if dfs(i, j):
                danji.append(cnt)
                cnt = 0

    print(len(danji))
    danji.sort()
    for i in danji:
        print(i)
