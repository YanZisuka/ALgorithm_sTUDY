import sys
input = sys.stdin.readline


arr = list(map(int, list(input().strip())))
arr.sort(reverse=True)
print(''.join(map(str, arr)))