def DFS(row, col):
    global matrix
    global cnt

    d_row = [0, 0, 1, -1]
    d_col = [1, -1, 0, 0]

    if 0 <= row < len(matrix) and 0 <= col < len(matrix) and matrix[row][col] == 1:

        cnt += 1
        matrix[row][col] = 0
        for i in range(4):
            n_row = row + d_row[i]
            n_col = col + d_col[i]
            DFS(n_row, n_col)
        return True


N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]

cnt = 0
result = 0
num = []

for row in range(N):
    for col in range(N):
        if DFS(row, col) == True:
            num.append(cnt)
            result += 1
            cnt = 0

num.sort()

print(result)
for i in range(len(num)):
    print(num[i])
