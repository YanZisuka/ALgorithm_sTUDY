import sys
sys.stdin = open('input.txt')


t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    cnt = 0
    
    for i in range(n):
        if m & (1 << i):
            cnt += 1
            
    if cnt == n:
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')