import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
arr = list(map(int, input().split()))
v = int(input())

print(arr.count(v))
