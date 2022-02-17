import sys
sys.stdin = open('input.txt')


def fund(n, arr):
    # stock = 0
    # budget = 0
    # for i in range(n):
    #     if arr[i] != max(arr[i:]):
    #         stock += 1
    #         budget -= arr[i]
    #     else:
    #         budget += arr[i] * stock
    #         stock = 0
    arr = arr[::-1]
    sell_price = arr[0]
    profit = 0
    for i in range(1, n):
        if arr[i] > sell_price:
            sell_price = arr[i]
        profit += sell_price - arr[i]
        
    return profit


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    
    print(f'#{tc} {fund(n, arr)}')