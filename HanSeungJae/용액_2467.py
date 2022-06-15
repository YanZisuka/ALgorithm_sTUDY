import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
minv = float('inf')

st, en = 0, n-1
while st < en:
    sumv = arr[st] + arr[en]
    if abs(sumv) < minv:
        minv = abs(sumv)
        answer = [arr[st], arr[en]]

    if sumv > 0:
        en -= 1
    else:
        st += 1

print(*answer)
