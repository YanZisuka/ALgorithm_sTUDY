import sys
sys.stdin = open('input.txt')


def max_len(arr):
    max_len = 0
    for i in range(5):
        if len(arr[i]) > max_len:
            max_len = len(arr[i])
    return max_len


def preProcessing(arr):
    length = max_len(arr)
    for j in range(5):
        if len(arr[j]) < length:
            arr[j] += [''] * (length - len(arr[j]))
    return arr


def arrColumn(arr):
    arr_column = []
    for j in range(max_len(arr)):
        for i in range(5):
            arr_column.append(arr[i][j])
    return ''.join(arr_column)


t = int(input())
for tc in range(1, t+1):
    arr = [list(input()) for _ in range(5)]
    arr = preProcessing(arr)
     
    print(f'#{tc} {arrColumn(arr)}')