import sys
sys.stdin = open('input.txt')


def dfs(i, cnt):
    global ans
    if cnt >= ans:
        return
    
    if i + stops[i] >= n:
        ans = min(cnt, ans)
        return
    
    for j in range(1, stops[i] + 1):
        dfs(i+j, cnt + 1)


t = int(input())
for tc in range(1, t+1):
    arr = list(map(int, input().split()))
    ans = float('inf')
    n = arr[0]
    stops = {i+1: 0 for i in range(n)}
    for i in range(1, len(arr)):
        stops[i] = arr[i]
        
    dfs(1, 0)
    print(f'#{tc} {ans}')