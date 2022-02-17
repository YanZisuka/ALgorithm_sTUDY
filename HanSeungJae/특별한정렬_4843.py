import sys
sys.stdin = open('input.txt')


def specialSort(n, arr):
    for i in range(10):
        max_val, min_val, idx = arr[i], arr[i], i
        if i % 2 == 0:
            for j in range(i, n):
                if arr[j] > max_val:
                    max_val, idx = arr[j], j
            arr[i], arr[idx] = arr[idx], arr[i]
        else:
            for j in range(i, n):
                if arr[j] < min_val:
                    min_val, idx = arr[j], j
            arr[i], arr[idx] = arr[idx], arr[i]
    return ' '.join(map(str, arr[:10]))


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    
    print(f'#{tc} {specialSort(n, arr)}')