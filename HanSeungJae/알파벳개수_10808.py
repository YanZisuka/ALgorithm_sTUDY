import sys
from string import ascii_lowercase
input = lambda: sys.stdin.readline().strip()


st = input()
table = {a: 0 for a in ascii_lowercase}

for char in st:
    table[char] += 1

print(*table.values())