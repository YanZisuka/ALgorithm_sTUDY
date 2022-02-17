import sys
sys.stdin = open('input.txt')


def set_matrix(n):
    matrix = [list(map(int, input().split())) for _ in range(n)]
    return matrix


def rotate_90_deg(n, matrix):
    matrix_rotated = []
    for j in range(n):
        row = []
        for i in range(n-1, -1, -1):
            row.append(matrix[i][j])
        matrix_rotated.append(row)
    return matrix_rotated


def postProcessing(n, mat_90, mat_180, mat_270):
    total_mat = []
    result = []
    for i in range(n):
        total_mat.append(mat_90[i] + [' '] + mat_180[i] + [' '] + mat_270[i])
    for j in range(n):
        result.append(''.join(map(str, total_mat[j])))
    return '\n'.join(result)


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    matrix = set_matrix(n)
    mat_90 = rotate_90_deg(n, matrix)
    mat_180 = rotate_90_deg(n, mat_90)
    mat_270 = rotate_90_deg(n, mat_180)
    
    print(f'#{tc}\n{postProcessing(n, mat_90, mat_180, mat_270)}')
    