def solution(n, build_frame):

    def check_col(si, sj):
        if si == n-1: return True
        if 1 <= sj < n and board_row[si+1][sj-1] == 1 or 0 <= sj < n and board_row[si+1][sj] == 1: return True
        if board_col[si+1][sj] == 1: return True
        return False
    
    def check_row(si, sj):
        if board_col[si][sj] == 1 or board_col[si][sj+1] == 1: return True
        if 1 <= sj < n-1 and board_row[si][sj-1] == 1 and board_row[si][sj+1] == 1: return True
        return False

    def build_col(x, y, state):
        sy = n - y - 1
        if state == 1:
            if check_col(sy, x):
                board_col[sy][x] = 1
                answer.append([x, y, 0])
        else:
            board_col[sy][x] = 0
            answer.remove([x, y, 0])
            for struc in answer:
                cx, cy, a = struc
                if a == 0:
                    ny = n - cy - 1
                    if not check_col(ny, cx):
                        board_col[sy][x] = 1
                        answer.append([x, y, 0])
                        return
                else:
                    ny = n - cy
                    if not check_row(ny, cx):
                        board_col[sy][x] = 1
                        answer.append([x, y, 0])
                        return
        
    def build_row(x, y, state):
        sy = n - y
        if state == 1:
            if check_row(sy, x):
                board_row[sy][x] = 1
                answer.append([x, y, 1])
        else:
            board_row[sy][x] = 0
            answer.remove([x, y, 1])
            for struc in answer:
                cx, cy, a = struc
                if a == 0:
                    ny = n - cy - 1
                    if not check_col(ny, cx):
                        board_row[sy][x] = 1
                        answer.append([x, y, 1])
                        return
                else:
                    ny = n - cy
                    if not check_row(ny, cx):
                        board_row[sy][x] = 1
                        answer.append([x, y, 1])
                        return
    

    answer = []

    board_col = [[0] * (n+1) for _ in range(n)]
    board_row = [[0] * n for _ in range(n+1)]

    for info in build_frame:
        x, y, a, b = info
        if a == 0:
            build_col(x, y, b)
        else:
            build_row(x, y, b)

    answer.sort(key=lambda x: (x[0], x[1], x[2]))

    return answer





print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))  # [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))  # [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
