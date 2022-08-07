import sys
from string import ascii_lowercase
def input(): return sys.stdin.readline().strip()


word1 = input()
word2 = input()
answer = 0

table1 = {a: 0 for a in ascii_lowercase}
table2 = {a: 0 for a in ascii_lowercase}

for char in word1:
    table1[char] += 1
for char in word2:
    table2[char] += 1

for a in ascii_lowercase:
    answer += abs(table1[a] - table2[a])

print(answer)
