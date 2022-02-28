N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]

d_row = [1, -1, 0, 0]
d_col = [0, 0, 1, -1]
queue = [[0, 0]]
maze[0][0] = 1

while queue:
    row = queue[0][0]
    col = queue[0][1]
    del queue[0]

    for i in range(4):
        n_row = row + d_row[i]
        n_col = col + d_col[i]

        if 0 <= n_row < N and 0 <= n_col < M and maze[n_row][n_col] == "1":
            queue.append([n_row, n_col])
            maze[n_row][n_col] = maze[row][col] + 1

print(maze[N - 1][M - 1])