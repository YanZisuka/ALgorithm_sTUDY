import sys
input = sys.stdin.readline


n, m = map(int, input().split())
answer = float('inf')

arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

st, en = 0, 0

while 0 <= st < n and 0 <= en < n:
    if arr[en] - arr[st] < m:
        en += 1
    elif arr[en] - arr[st] > m:
        answer = min(answer, arr[en] - arr[st])
        st += 1
    else:
        answer = m
        break

print(answer)