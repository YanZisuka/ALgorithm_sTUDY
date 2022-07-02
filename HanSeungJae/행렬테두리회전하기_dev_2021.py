def solution(rows, columns, queries):
    def rotate(x1, y1, x2, y2):
        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]
        i1, j1, i2, j2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        row_range, col_range = abs(j2 - j1), abs(i2 - i1)
        ci, cj = i1, j1

        tmp = matrix[ci][cj]
        val = tmp
        for k in range(4):
            if k % 2:
                for _ in range(col_range):
                    ni, nj = ci + di[k], cj + dj[k]
                    matrix[ni][nj], tmp = tmp, matrix[ni][nj]
                    val = min(val, tmp)
                    ci, cj = ni, nj
            else:
                for _ in range(row_range):
                    ni, nj = ci + di[k], cj + dj[k]
                    matrix[ni][nj], tmp = tmp, matrix[ni][nj]
                    val = min(val, tmp)
                    ci, cj = ni, nj
        return val


    answer = []
    matrix = [[0] * columns for _ in range(rows)]
    cnt = 1

    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = cnt
            cnt += 1

    for query in queries:
        answer.append(rotate(*query))

    return answer