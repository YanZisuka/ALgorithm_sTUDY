import sys
from string import ascii_uppercase

input = lambda: sys.stdin.readline().strip()


def my_sum(el):
    sumv = 0
    for char in el:
        if char not in ascii_uppercase:
            sumv += int(char)
    return sumv


n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

arr.sort(key=lambda x: (len(x), my_sum(x), x))

for el in arr:
    print(el)
