import sys
sys.stdin = open('input.txt')


def quickSort(arr):
    n = len(arr)
    if n <= 1: return arr

    pivot = n // 2

    left = []
    right = []
    center = []

    for num in arr:
        if num > arr[pivot]:
            right.append(num)
        elif num < arr[pivot]:
            left.append(num)
        elif num == arr[pivot]:
            center.append(num)

    return quickSort(left) + center + quickSort(right)


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = quickSort(arr)

    print(f'#{tc} {arr[n // 2]}')