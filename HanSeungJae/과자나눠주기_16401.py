import sys
input = sys.stdin.readline


def cut(key):
    cnt = 0

    for el in arr:
        if el >= key:
            cnt += el // key
    return cnt


m, n = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

st, en = 1, 1000000000

while st <= en:
    md = (st + en) // 2
    if cut(md) >= m:
        answer = md
        st = md + 1
    else: en = md - 1

print(answer)
