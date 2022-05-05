from collections import deque

def solution(places):

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    
    def bfs(si, sj):
        visited = [[False] * 5 for _ in range(5)]
        q = deque()
        q.append((si, sj))
        visited[si][sj] = True
        cnt = 0

        while q:
            r = len(q)
            for _ in range(r):
                ci, cj = q.popleft()
                for k in range(4):
                    ni = ci + di[k]
                    nj = cj + dj[k]
                    if 0 <= ni < 5 and 0 <= nj < 5 and not visited[ni][nj] and room[ni][nj] != 'X':
                        if room[ni][nj] == 'P':
                            return False
                        visited[ni][nj] = True
                        q.append((ni, nj))
            cnt += 1
            if cnt >= 2:
                return True

    def check(room):
        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':
                    result = bfs(i, j)
                    if result == False:
                        answer.append(0)
                        return
        answer.append(1)

    answer = []

    for i in range(len(places)):
        room = places[i]
        check(room)

    return answer