import sys
input = sys.stdin.readline


def binarySearch(target, endPoint):
    start = 0
    end = endPoint - 1
    location = -1
    
    while start <= end:
        mid = (start + end) // 2
        if oven[mid] >= target:
            start = mid + 1
            location = mid
        elif oven[mid] < target:
            end = mid - 1

    return location


d, n = map(int, input().split())
oven = list(map(int, input().split()))
doughs = list(map(int, input().split()))

for i in range(1, d):
    if oven[i] > oven[i-1]:
        oven[i] = oven[i-1]

answer = 0
endPoint = d

for dough in doughs:
    tmp = binarySearch(dough, endPoint)
    if tmp == -1:
        continue
    answer = tmp
    endPoint = answer

if answer != 0:
    answer += 1
print(answer)
