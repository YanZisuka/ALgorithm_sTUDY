import sys
def my_fact(n):
    if n < 2:
        return 1
    else:
        return n * my_fact(n-1)
    
input = sys.stdin.readline

n = int(input())
print(my_fact(n))