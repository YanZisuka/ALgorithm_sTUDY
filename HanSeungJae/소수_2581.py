import sys
input = sys.stdin.readline


def isPrime(x):
    if x < 2:
        return False
    
    n = 2
    while n ** 2 <= x:
        if x % n == 0:
            return False
        n += 1
    return True


m = int(input())
n = int(input())
sumValue = 0
minPrimeNum = float('inf')

for i in range(m, n+1):
    if isPrime(i):
        sumValue += i
        minPrimeNum = min(minPrimeNum, i)

if sumValue:
    print(sumValue, minPrimeNum, sep='\n')
else:
    print(-1)
