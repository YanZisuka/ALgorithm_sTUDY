import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
minv = float('inf')
answer = [0, 0]

st, en = 0, n-1

while st < en:
    sumv = arr[st] + arr[en]

    if minv > abs(sumv):
        minv = abs(sumv)
        answer[0] = arr[st]
        answer[1] = arr[en]

        if sumv == 0:
            break

    if sumv < 0:
        st += 1
    else:
        en -= 1

print(*answer)