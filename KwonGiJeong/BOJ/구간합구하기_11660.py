def get_part_sum(matrix, first_row, first_col, last_row, last_col):
    sum = 0
    for row in range(first_row - 1, last_row):
        for col in range(first_col - 1, last_col):
            sum += matrix[row][col]

    return sum



N, M = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(N)]

ranges = [list(map(int,input().split())) for _ in range(M)]

for i in range(M):
    print(get_part_sum(matrix, ranges[i][0], ranges[i][1], ranges[i][2], ranges[i][3]))