import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = list(map(int, input().split()))
psums = arr[:]
answer = 0

for i, e in enumerate(psums):
    if i != 0:
        psums[i] += psums[i-1]

st, en = 0, 0
while st < n and en < n:
    psum = psums[en] - psums[st] + arr[st]
    if psum == m:
        answer += 1
        if st < en:
            st += 1
        else:
            en += 1
    elif psum > m:
        st += 1
    elif psum < m:
        en += 1

print(answer)
