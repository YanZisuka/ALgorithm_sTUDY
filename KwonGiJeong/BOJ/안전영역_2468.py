import sys

sys.stdin = open('input_2468.txt')

def DFS(row, col, level):
    global visited

    visited[row][col] = 1

    d_row = [0, 0, 1, -1]
    d_col = [1, -1, 0, 0]

    for i in range(4):
        n_row = row + d_row[i]
        n_col = col + d_col[i]

        if 0 <= n_row < len(matrix) and 0 <= n_col < len(matrix) and matrix[n_row][n_col] > level and visited[n_row][n_col] == 0:
            DFS(n_row, n_col, level)


N = int(input())
matrix = [list(map(int, input().split(' '))) for _ in range(N)]

# 수위가 될 집합들(Back Tracking)
levels = set()
for row in range(N):
    for col in range(N):
        levels.add(matrix[row][col])

result = 0

for level in levels:
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for row in range(N):
        for col in range(N):
            if matrix[row][col] > level and visited[row][col] == 0:
                DFS(row, col, level)
                cnt += 1

    if cnt > result:
        result = cnt

print(result)

