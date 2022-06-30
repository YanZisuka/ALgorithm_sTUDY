import sys
from itertools import combinations
input = lambda: sys.stdin.readline().strip()


l, c = map(int, input().split())
arr = input().split()
answer = set()

for case in combinations(arr, l):
    case = sorted(list(case))
    pwd = ''.join(case)

    ccnt, vcnt = 0, 0
    for char in pwd:
        if char in ['a', 'e', 'i', 'o', 'u']:
            vcnt += 1
        else:
            ccnt += 1
    
    if ccnt >= 2 and vcnt >= 1: answer.add(pwd)

answer = sorted(list(answer))

for el in answer: print(el)