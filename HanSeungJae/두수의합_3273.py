import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
x = int(input())

l, r = 0, n-1
answer = 0

while True:
    if l >= r:
        break
    if arr[l] + arr[r] == x:
        answer += 1
        l += 1
        r -= 1
    elif arr[l] + arr[r] < x:
        l += 1
    else:
        r -= 1

print(answer)
