from collections import deque
import sys
sys.stdin = open('input.txt')


def bfs(n, cnt):
    global ans
    
    queue = deque()
    queue.append((n, cnt))
    visited[n] = True
    
    while queue:
        num, cnt = queue.popleft()
        if num == m:
            ans = min(ans, cnt)
            return
        
        if num + 1 <= 1000000 and not visited[num+1]:
            visited[num+1] = True
            queue.append((num+1, cnt+1))
        if num * 2 <= 1000000 and not visited[num*2]:
            visited[num*2] = True
            queue.append((num*2, cnt+1))
        if 0 < num - 1 and not visited[num-1]:
            visited[num-1] = True
            queue.append((num-1, cnt+1))
        if 0 < num - 10 and not visited[num-10]:
            visited[num-10] = True
            queue.append((num-10, cnt+1))
        

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    ans = float('inf')
    visited = [False] * 1000001
    
    bfs(n, 0)
    
    print(f'#{tc} {ans}')
    
    