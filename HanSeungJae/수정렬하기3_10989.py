import sys
def input(): return sys.stdin.readline().strip()


NUM = 10001
n = int(input())
arr = [0] * NUM
for _ in range(n):
    arr[int(input())] += 1

for i in range(NUM):
    for _ in range(arr[i]):
        print(i)
