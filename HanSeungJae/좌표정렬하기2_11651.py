import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort(key=lambda x: (x[1], x[0]))
for el in arr:
    print(*el)
