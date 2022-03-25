import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    day, mon, mon3, year = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    
    dp = [0] * 13
    
    for i in range(1, 13):
        min_val = dp[i-1] + arr[i] * day
        min_val = min(min_val, dp[i-1] + mon)
        
        if i >= 3:
            min_val = min(min_val, dp[i - 3] + mon3)
            
        if i >= 12:
            min_val = min(min_val, dp[i - 12] + year)
            
        dp[i] = min_val
        
    print(f'#{tc} {dp[12]}')