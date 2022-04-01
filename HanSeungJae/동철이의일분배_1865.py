import sys
sys.stdin = open('input.txt')


def dfs(i, per):
    global ans
    if 1-per >= ans:
        return
    
    if i == n:
        ans = min(ans, 1-per)
        return
        
    for j in range(n):
        if not visited[j]:
            visited[j] = True
            dfs(i+1, per * arr[i][j])
            visited[j] = False


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    for i in range(n):
        arr[i] = list(map(lambda x: x*0.01, arr[i]))
    ans = float('inf')  # 일이 하나라도 실패할 확률
    
    dfs(0, 1)
    
    ans = 1 - ans  # 일이 성공할 확률로 변환
    print(f'#{tc} {ans*100:.6f}')
    