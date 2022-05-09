import sys
input = sys.stdin.readline


n = int(input())
requests = list(map(int, input().split()))
m = int(input())
answer = 0

if sum(requests) <= m:
    print(max(requests))
else:
    start = 1
    end = 100000

    while start <= end:
        mid = (start + end) // 2
        tmp = 0
        for i in range(n):
            if mid < requests[i]:
                tmp += mid
            else:
                tmp += requests[i]
        if tmp == m:
            answer = mid
            break
        elif tmp < m:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    print(answer)