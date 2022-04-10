import sys
from collections import deque
input = sys.stdin.readline


def topologySort():
    q = deque()
    
    for i in range(1, n+1):
        if inDegree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        answer.append(cur)

        for nxt in graph[cur]:
            inDegree[nxt] -= 1
            if inDegree[nxt] == 0:
                q.append(nxt)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
inDegree = [0] * (n+1)
answer = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

topologySort()

print(' '.join(map(str, answer)))