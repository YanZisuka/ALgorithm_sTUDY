import sys
sys.stdin = open('input.txt')


def get_matrix_sum(matrix):
    sum_list = []

    for i in range(100):
        total = 0
        for j in range(100):
            total += matrix[i][j]
        sum_list.append(total)

    for j in range(100):
        total = 0
        for i in range(100):
            total += matrix[i][j]
        sum_list.append(total)

    total = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                total += matrix[i][j]
    sum_list.append(total)

    total = 0
    for i in range(100):
        for j in range(99, -1, -1):
            if i == 99 - j:
                total += matrix[i][j]
    sum_list.append(total)
    
    return max(sum_list)


for tc in range(1, 11):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    
    print(f'#{n} {get_matrix_sum(matrix)}')