import sys
input = sys.stdin.readline


def lower_bound(t):
    st, en = 0, n-1
    while st < en:
        md = (st + en) // 2
        if cards[md] >= t: en = md
        else: st = md + 1
    return en


def upper_bound(t):
    st, en = 0, n-1
    while st < en:
        md = (st + en) // 2
        if cards[md] > t: en = md
        else: st = md + 1
    return en


n = int(input())
cards = list(map(int, input().split()))
cards.sort()
m = int(input())
targets = list(map(int, input().split()))
answer = []

for t in targets:
    u = upper_bound(t)
    b = lower_bound(t)
    if u == n - 1 and t == cards[n - 1]:
        u += 1
    answer.append(u - b)
print(*answer)

"""
import sys
input = sys.stdin.readline


n = int(input())
table = {}
for card in list(map(int, input().split())):
    if table.get(card): table[card] += 1
    else: table[card] = 1
m = int(input())
for t in list(map(int, input().split())):
    if table.get(t): print(table[t], end=' ')
    else: print(0, end=' ')
print()

"""