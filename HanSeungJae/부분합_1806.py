import sys
input = sys.stdin.readline


n, s = map(int, input().split())
arr = list(map(int, input().split()))
answer = float('inf')

en = 0
tot = arr[0]

for st in range(n):
    while en < n and tot < s:
        en += 1
        if en != n:
            tot += arr[en]

    if en == n: break

    answer = min(answer, en - st + 1)
    tot -= arr[st] 

if answer >= float('inf'): answer = 0

print(answer)
        
