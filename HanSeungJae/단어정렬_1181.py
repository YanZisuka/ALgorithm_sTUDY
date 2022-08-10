import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
arr = set()
for _ in range(n):
    arr.add(input())

arr = list(arr)
arr.sort(key=lambda x: (len(x), x))

for el in arr:
    print(el)
