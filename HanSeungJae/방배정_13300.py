import sys
import math
input = lambda: sys.stdin.readline().strip()


n, k = map(int, input().split())
table = {}
for si in range(2):
    for yi in range(1, 7):
        key = str(si) + str(yi)
        table[key] = []

for i in range(n):
    s, y = map(int, input().split())
    key = str(s) + str(y)
    table[key].append(i)

answer = 0
for v in table.values():
    if len(v) == 0: continue
    answer += math.ceil(len(v) / k)

print(answer)