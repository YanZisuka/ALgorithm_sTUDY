import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

di = [-2, -1, -2, -1, 1, 2, 1, 2]
dj = [-1, -2, 1, 2, -2, -1, 2, 1]

def bfs(si, sj):
    dist = [[-1] * l for _ in range(l)]
    cnt = 0
    q = deque()
    q.append((si, sj))
    dist[si][sj] = cnt

    while q:
        cnt += 1
        r = len(q)
        for _ in range(r):
            ci, cj = q.popleft()

            if (ci, cj) == goal: return dist[ci][cj]

            for k in range(8):
                ni = ci + di[k]
                nj = cj + dj[k]
                if 0 <= ni < l and 0 <= nj < l and dist[ni][nj] == -1:
                    dist[ni][nj] = cnt
                    q.append((ni, nj))


t = int(input())
for tc in range(1, t+1):
    l = int(input())
    board = [[0] * l for _ in range(l)]
    start = tuple(map(int, input().split()))
    goal = tuple(map(int, input().split()))

    print(bfs(*start))

