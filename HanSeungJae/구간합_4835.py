def my_max(*args):
    list_ = list(map(int, *args))
    max_ = list_[0]

    for i in range(len(list_)):
        if list_[i] > max_:
            max_ = list_[i]

    return max_


def my_min(*args):
    list_ = list(map(int, *args))
    min_ = list_[0]

    for i in range(len(list_)):
        if list_[i] < min_:
            min_ = list_[i]

    return min_


def interval_sum(n, m, arr):
    sum_list = []

    for i in range(n - m + 1):
        sum_list.append(sum(arr[i:i + m]))

    return my_max(sum_list) - my_min(sum_list)


t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    print(f'#{tc} {interval_sum(n, m, arr)}')