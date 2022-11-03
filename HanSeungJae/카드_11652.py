import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
table = {}
maxk, maxv = None, None
for _ in range(n):
    num = int(input())
    if table.get(num):
        table[num] += 1
    else:
        table[num] = 1
    if table[num] > maxv:
        maxk = num
        maxv = table[num]
    elif table[num] == maxv:
        maxk = min(maxk, num)

print(maxk)
