from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def control(dir, color, redPos, bluePos):
    if color == 'red':
        ci, cj = redPos
    elif color == 'blue':
        ci, cj = bluePos

    if (ci, cj) == goal:
        return ci, cj

    while True:
        ni = ci + di[dir]
        nj = cj + dj[dir]

        if board[ni][nj] == 'O':
            return ni, nj
        if board[ni][nj] == '#' or (ni, nj) == redPos or (ni, nj) == bluePos:
            break
        ci, cj = ni, nj
    return ci, cj
            
    
def dfs(step, redPos, bluePos):
    global answer

    if step >= answer:
        return

    if step > 10:
        return

    for k in range(4):
        redTemp = control(k, 'red', redPos, bluePos)
        blueTemp = control(k, 'blue', redTemp, bluePos)
        redTemp = control(k, 'red', redTemp, blueTemp)
        if redTemp == goal and blueTemp != goal:
            answer = min(answer, step)
            return
        dfs(step+1, redTemp, blueTemp)


def bfs(redPos, bluePos):
    global answer

    ri, rj = redPos
    bi, bj = bluePos

    q = deque()
    q.append((1, ri, rj, bi, bj))
    visited[ri][rj][bi][bj] = True
    
    while q:
        step, ri, rj, bi, bj = q.popleft()

        if step > 10:
            return

        for k in range(4):
            nri, nrj = control(k, 'red', (ri, rj), (bi, bj))
            nbi, nbj = control(k, 'blue', (nri, nrj), (bi, bj))
            nri, nrj = control(k, 'red', (nri, nrj), (nbi, nbj))
            if (nri, nrj) == goal and (nbi, nbj) != goal:
                answer = min(answer, step)
                return
            if not visited[nri][nrj][nbi][nbj]:
                visited[nri][nrj][nbi][nbj] = True
                q.append((step+1, nri, nrj, nbi, nbj))
            

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
answer = float('inf')

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            redPos = (i, j)
        elif board[i][j] == 'B':
            bluePos = (i, j)
        elif board[i][j] == 'O':
            goal = (i, j)

bfs(redPos, bluePos)

if answer >= float('inf'):
    answer = -1

print(answer)
