def DFS(row, col, cnt):

    global alphabets
    global result

    if cnt > result:
        result = cnt

    d_row = [0, 0, 1, -1]
    d_col = [1, -1, 0, 0]

    for i in range(4):
        n_row = row + d_row[i]
        n_col = col + d_col[i]

        if 0 <= n_row < len(matrix) and 0 <= n_col < len(matrix[0]) and not matrix[n_row][n_col] in alphabets:
            alphabets.add(matrix[n_row][n_col])
            DFS(n_row, n_col, cnt+1)
            alphabets.remove(matrix[n_row][n_col])

R, C = map(int, input().split())
matrix = []
for _ in range(R):
    matrix.append(list(input()))

result = 0
alphabets = set(matrix[0][0])

DFS(0, 0, 1)
print(result)
