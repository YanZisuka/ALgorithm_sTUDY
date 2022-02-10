def max_min_gap(arr):
    min_ = arr[0]
    max_ = arr[0]

    for i in range(len(arr)):
        if arr[i] < min_:
            min_ = arr[i]
        if arr[i] > max_:
            max_ = arr[i]

    return max_ - min_


t = int(input())

for _ in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))

    print(f'#{_} {max_min_gap(arr)}')