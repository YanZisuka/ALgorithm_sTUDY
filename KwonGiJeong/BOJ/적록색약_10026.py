def Normaldfs(row, col):
    global Normalvisited

    Normalvisited[row][col] = 1

    for i in range(4):
        n_row = row + d_row[i]
        n_col = col + d_col[i]

        if 0 <= n_row < N and 0 <= n_col < N and matrix[row][col] == matrix[n_row][n_col] and Normalvisited[n_row][n_col] == 0:
            Normaldfs(n_row, n_col)

def RGdfs(row, col):
    global RGvisited

    RGvisited[row][col] = 1
    if matrix[row][col] == 'R' or matrix[row][col] == 'G':
        odd = True

    else:
        odd = False

    for i in range(4):
        n_row = row + d_row[i]
        n_col = col + d_col[i]

        if 0 <= n_row < N and 0 <= n_col < N and RGvisited[n_row][n_col] == 0:
            if odd == True:
                if matrix[n_row][n_col] == 'R' or matrix[n_row][n_col] == 'G':
                    RGdfs(n_row, n_col)
            else:
                if matrix[row][col] == matrix[n_row][n_col]:
                    RGdfs(n_row, n_col)

N = int(input())
matrix = [list(input()) for _ in range(N)]

Normalvisited = [[0] * N for _ in range(N)]
RGvisited = [[0] * N for _ in range(N)]

d_row = [0, 0, 1, -1]
d_col = [1, -1, 0, 0]

Normalcnt = 0
for row in range(N):
    for col in range(N):
        if Normalvisited[row][col] == 0:
            Normaldfs(row, col)
            Normalcnt += 1

RGcnt = 0
for row in range(N):
    for col in range(N):
        if RGvisited[row][col] == 0:
            RGdfs(row, col)
            RGcnt += 1



print(Normalcnt, end=" ")
print(RGcnt)