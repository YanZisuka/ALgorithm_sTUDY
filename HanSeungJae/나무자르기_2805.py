import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

st, en = 0, 1000000000
while st <= en:
    md = (st + en) // 2
    cnt = 0
    for el in arr:
        if el > md:
            cnt += el - md
    if cnt >= m:
        answer = md
        st = md + 1
    else:
        en = md - 1

print(answer)