import sys
input = sys.stdin.readline


n = int(input())
lst = []

for _ in range(n):
    age, name = input().split()
    lst.append([age, name])
    
lst.sort(key=lambda x: int(x[0]))

for member in lst:
    print(*member)