import sys
input = sys.stdin.readline


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.sort()
answer = []

for el in a:
    st, en = 0, m-1
    find = False
    while st <= en:
        md = (st + en) // 2
        if b[md] == el:
            find = True
            break
        elif b[md] < el: st = md + 1
        else: en = md - 1
    if find == False: answer.append(el)

answer.sort()

if answer:
    print(len(answer))
    print(*answer)
else: print(0)

"""
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
s = a - b

print(len(s))
print(*sorted(s))
"""