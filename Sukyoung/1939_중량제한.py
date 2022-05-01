import sys
input = sys.stdin.readline
from collections import deque

def bfs(mid):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        node = queue.popleft()
        if node == end:  # 목적지에 도착하면 True
            return 1
        for b in bridge[node]:
            if visited[b[0]] == 0 and b[1] >= mid:
                queue.append(b[0])
                visited[b[0]] = 1
    return 0

N, M = map(int,input().split())
bridge = [[] for _ in range(N+1)]
for i in range(M):
    A, B, C = map(int,input().split())
    bridge[A].append([B,C])
    bridge[B].append([A,C])
start,end = map(int,input().split())

min_limit = 1
max_limit = 1000000000
while min_limit <= max_limit:  # mid값으로 목적지에 도착할 수 있는지 판별
    visited = [0] * (N + 1)
    mid = (min_limit + max_limit) // 2
    if bfs(mid):  # 도착할 수 있으면,
        min_limit = mid+1  # 더 큰 범위 탐색
    else:  # 도착할 수 없으면,
        max_limit = mid-1  # 작은 범위 탐색
print(max_limit)

# 이분탐색 안쓰고 dfs -> 메모리 초과
# def dfs(start):
#     visited[start] = 1
#     if start == end:
#         return
#     for i in bridge[start]:
#         if visited[i] == 0:
#             limit[i] = max(limit[i], min(limit[start],max_limit[min(start,i)][max(start,i)]))
#             visited[i] = 1
#             dfs(i)
#             visited[i] = 0
#
# N, M = map(int,input().split())
# bridge = [set() for _ in range(N+1)]
# visited = [0] * (N+1)
# limit = [0]*(N+1)
# max_limit = [[0]*(N+1) for _ in range(N+1)]
# for i in range(M):
#     A, B, C = map(int,input().split())
#     if max_limit[min(A,B)][max(A,B)] < C:
#        max_limit[min(A,B)][max(A,B)] = C
#     bridge[A].add(B)
#     bridge[B].add(A)
#
# start,end = map(int,input().split())
# limit[start] = float('inf')
# dfs(start)
# print(limit[end])
