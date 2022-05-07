from collections import deque

def solution(numbers, hand):
    
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    def bfs(si, sj):
        visited = [[False] * 3 for _ in range(4)]
        q = deque()
        q.append((si, sj))
        visited[si][sj] = True
        cnt = 0
        left_dist, right_dist = 0, 0

        while q:
            r = len(q)
            for _ in range(r):
                ci, cj = q.popleft()
                if board[ci][cj] == left:
                    left_dist = cnt
                elif board[ci][cj] == right:
                    right_dist = cnt

                for k in range(4):
                    ni = ci + di[k]
                    nj = cj + dj[k]
                    if 0 <= ni < 4 and 0 <= nj < 3 and not visited[ni][nj]:
                        visited[ni][nj] = True
                        q.append((ni, nj))
            cnt += 1
        return (left_dist, right_dist)

    answer = ''
    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ['*', 0, '#']
        ]
    left = '*'
    right = '#'

    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left = number
        elif number in [3, 6, 9]:
            answer += 'R'
            right = number
        else:
            for i in range(4):
                for j in range(3):
                    if board[i][j] == number:
                        left_dist, right_dist = bfs(i, j)
                        if left_dist == right_dist:
                            if hand == 'right':
                                answer += 'R'
                                right = number
                            elif hand == 'left':
                                answer += 'L'
                                left = number
                        elif left_dist > right_dist:
                            answer += 'R'
                            right = number
                        elif left_dist < right_dist:
                            answer += 'L'
                            left = number

    return answer