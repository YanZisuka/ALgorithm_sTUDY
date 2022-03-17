from collections import deque
import sys
sys.stdin = open('input.txt')


def setGraph(input_str):
    for i in range(n):
        if i % 2:
            _from = input_str[i - 1]
            _to = input_str[i]
            
            graph[_from].append(_to)


def bfs(start):
    queue = deque()
    visited[start] = True
    
    if graph[start]:
        for next in graph[start]:
            if not visited[next]:
                queue.append(next)
    else:
        return start
    
    radius = 0
    
    while queue:
        r = len(queue)  # r마다 radius += 1
        last = []
        radius += 1
        
        for i in range(r):  # for문을 통해 반경마다 dist += 1
            now = queue.popleft()
            
            if not visited[now]:  # 실제로 연락이 들어가면
                visited[now] = True
                last.append(now)  # 마지막으로 연락받은 사람 목록에 추가
                for next in graph[now]:
                    if not visited[next]:
                        queue.append(next)
                
    return max(last)
            

for tc in range(1, 11):
    n, start = map(int, input().split())
    graph = [[] for _ in range(101)]
    visited = [False] * 101
    visited[0] = True
    
    input_str = list(map(int, input().split()))
    setGraph(input_str)
            
    
    print(f'#{tc} {bfs(start)}')
