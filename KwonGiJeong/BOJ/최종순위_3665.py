import sys
from collections import deque
input = sys.stdin.readline


def topologySort():
    ans = []
    queue = deque()

    for i in range(1, n+1):
        if inDegree[i] == 0:
            queue.append(i)

    while queue:

        now = queue.popleft()
        ans.append(now)

        for nxt in graph[now]:
            inDegree[nxt] -= 1
            if inDegree[nxt] == 0:
                queue.append(nxt)

    return ans


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    rank = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    inDegree = [0] * (n+1)

    # 순위가 주워 졌을 때, 각각의 승부를 모두 기록해 준다.
    for i in range(n-1):
        for j in range(i+1, n):
            graph[rank[i]].append(rank[j])
            inDegree[rank[j]] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())

        # 순위가 바뀌는 경우 진입과 그래프 기록을 바꿔준다.
        if b in graph[a]:
            graph[a].remove(b)
            graph[b].append(a)
            inDegree[b] -= 1
            inDegree[a] += 1
        else:
            graph[b].remove(a)
            graph[a].append(b)
            inDegree[a] -= 1
            inDegree[b] += 1

    ans = topologySort()

    if len(ans) == n:
        print(' '.join(map(str, ans)))
    else:
        print('IMPOSSIBLE')