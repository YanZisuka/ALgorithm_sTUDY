def my_max(*args):
    list_ = list(map(int, *args))
    max_ = list_[0]
    
    for i in range(len(list_)):
        if list_[i] > max_:
            max_ = list_[i]
        
    return max_


def view(length, arr):
    cnt = 0
    for i in range(2, length - 2):  # 좌, 우 2칸은 건물이 없으므로 제외
        if arr[i] > arr[i - 2] and arr[i] > arr[i - 1] and arr[i] > arr[i + 1] and arr[i] > arr[i + 2]:
            cnt += arr[i] - my_max([arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2]])

    return cnt


for tc in range(1, 11):
    length = int(input())
    arr = list(map(int, input().split()))
    
    print(f'#{tc} {view(length, arr)}')
    