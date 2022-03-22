import sys
sys.stdin = open('input.txt')


def solution(customers):
    stock = 0
    time = customers[0] % m
    stock += k * (customers[0] // m)
    
    for i in range(n):
        customer = customers[i]
        
        if 0 < i < n:
            time += customer - customers[i-1]
        
        if time // m:
            stock += k * (time // m)
            time = time % m
            
        if stock:
            stock -= 1
        else:
            return 'Impossible'
    
    return 'Possible'


t = int(input())
for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    customers = list(map(int, input().split()))
    customers.sort()
    
    print(f'#{tc} {solution(customers)}')