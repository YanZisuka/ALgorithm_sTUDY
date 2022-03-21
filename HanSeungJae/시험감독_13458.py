import sys, math
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
cnt = n

for i in range(n):
    if a[i] >= b:
        m = (a[i] - b) / c
    else:
        m = 0
        
    gap = m - int(m)

    if not math.isclose(0, gap):
        m = int(m) + 1
    else:
        m = int(m)
    
    cnt += m

print(cnt)