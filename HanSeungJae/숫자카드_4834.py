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


def num_card(n, arr):
    cnts = [0] * 10

    for num in arr:
        cnts[num] += 1

    for i in range(9, -1, -1):
        if cnts[i] == my_max(cnts):
            return i, cnts[i]


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input()))
    
    print(f'#{tc} {num_card(n, arr)[0]} {num_card(n, arr)[1]}')