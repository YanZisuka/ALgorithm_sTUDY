import sys
sys.stdin = open('input.txt', 'r')

di = [1, 1, -1, -1, 1]
dj = [-1, 1, 1, -1, -1]


def dfs(n, ci, cj, v, cnt):
    global si, sj, ans
    
    if n == 2 and ans >= cnt * 2:
        return
    if n > 3:
        return
    if ci == si and cj == sj and n == 3 and ans < cnt:
        ans = cnt
        return
    
    for k in range(n, n+2):
        ni, nj = ci + di[k], cj + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] not in v:
                v.append(arr[ni][nj])
                dfs(k, ni, nj, v, cnt + 1)
                v.pop()


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    
    for si in range(0, N-2):
        for sj in range(1, N-1):
            dfs(0, si, sj, [], 0)
            
    print(f'#{tc} {ans}')