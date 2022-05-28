import sys
input = sys.stdin.readline


def binary_search(arr, k):
    st, en = 0, len(arr)-1
    while st <= en:
        md = (st + en) // 2
        if arr[md] == k: return 1
        elif arr[md] < k: st = md + 1
        else: en = md - 1
    return 0


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
keys = list(map(int, input().split()))

for key in keys:
    print(binary_search(arr, key))
