import sys
input = sys.stdin.readline


def binary_search(arr, t):
    st, en = 0, len(arr) - 1
    while st < en:
        md = (st + en) // 2
        if arr[md] >= t: en = md
        else: st = md + 1
    return en


n = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(list(set(arr)))
answer = []

for el in arr:
    answer.append(binary_search(sorted_arr, el))
print(*answer)
