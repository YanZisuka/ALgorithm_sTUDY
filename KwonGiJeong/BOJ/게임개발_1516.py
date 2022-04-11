import sys
from collections import deque

input = sys.stdin.readline


def topologySort():
    result = [0] * (n + 1)
    queue = deque()

    for i in range(1, n + 1):
        if inDegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        result[now] += cost[now]

        for nxt in graph[now]:
            inDegree[nxt] -= 1
            result[nxt] = max(result[nxt], result[now])
            if inDegree[nxt] == 0:
                queue.append(nxt)

    return result


n = int(input())
graph = [[] for _ in range(n + 1)]
inDegree = [0] * (n + 1)
cost = [0] * (n + 1)

for i in range(1, n + 1):
    info = list(map(int, input().split()))
    cost[i] = info[0]

    j = 1
    while info[j] != -1:
        graph[info[j]].append(i)
        inDegree[i] += 1
        j += 1

answer = topologySort()

for i in range(1, n + 1):
    print(answer[i])