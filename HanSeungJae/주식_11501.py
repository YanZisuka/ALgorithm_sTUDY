import sys
def input(): return sys.stdin.readline().strip()


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    maxv = 0

    for i in range(n-1, 0, -1):
        price = arr[i]

        if price > arr[i-1]:
            maxv = max(maxv, price)
            answer += maxv - arr[i-1]
        elif maxv > arr[i-1]:
            answer += maxv - arr[i-1]

    print(answer)
