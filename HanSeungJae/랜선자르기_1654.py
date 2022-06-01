import sys
input = sys.stdin.readline


k, n = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))

LIMIT = 2 ** 31 - 1
st, en = 1, LIMIT
answer = 0

while st <= en:
    md = (st + en) // 2
    cnt = 0
    for a in arr:
        cnt += a // md
    if cnt >= n:
        st = md + 1
        answer = max(answer, md)
    else: en = md - 1

print(answer)
