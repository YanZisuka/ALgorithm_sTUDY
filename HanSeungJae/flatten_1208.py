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


def flatten(dump_num, arr):
    for _ in range(dump_num):
        arr[arr.index(my_max(arr))] -= 1
        arr[arr.index(my_min(arr))] += 1

        if my_max(arr) - my_min(arr) < 2:
            return my_max(arr) - my_min(arr)
    return my_max(arr) - my_min(arr)


for tc in range(1, 11):
    dump_num = int(input())
    arr = list(map(int, input().split()))
    
    print(f'#{tc} {flatten(dump_num, arr)}')