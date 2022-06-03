"""
def solution(key, lock):

    m, n = len(key), len(lock)

    def rotate(key):
        new_key = []
        for j in range(m):
            row = []
            for i in range(m-1, -1, -1):
                row.append(key[i][j])
            new_key.append(row)
        return new_key

    
    def mask(key):
        msk = []
        for i in range(m):
            for j in range(m):
                if key[i][j] == 1:
                    msk.append([i, j])
        oi, oj = msk[0][0], msk[0][1]
        for el in msk:
            el[0] -= oi
            el[1] -= oj
        return msk
    

    rotated_key = key
    for _ in range(4):
        rotated_key = rotate(rotated_key)
        msk = mask(rotated_key)

        for di in range(m):
            for dj in range(m):
                new_key = [[0] * m for _ in range(m)]
                for i, j in msk:
                    ci, cj = i + di, j + dj
                    if 0 <= ci < m and 0 <= cj < m:
                        new_key[ci][cj] = 1

                judge = [[0] * n for _ in range(n)]
                for li in range(n):
                    for lj in range(n):
                        if 0 <= li < m and 0 <= lj < m:
                            judge[li][lj] = new_key[li][lj] + lock[li][lj]
                        else:
                            judge[li][lj] = lock[li][lj]
                print(judge)
                            
                cnt = 0
                for li in range(n):
                    if 0 in judge[li] or 2 in judge[li]:
                        cnt = 1
                        break
                if cnt == 0: 
                    return True

    return False
"""

def solution(key, lock):

    def unlock(si, sj, key):
        for i in range(m):
            for j in range(m):
                board[si + i][sj + j] += key[i][j]

    def relock(si, sj, key):
        for i in range(m):
            for j in range(m):
                board[si + i][sj + j] -= key[i][j]

    def rotate(mat):
        return list(zip(*mat[::-1]))

    def check():
        for i in range(n):
            for j in range(n):
                if board[m+i][m+j] != 1: return False
        return True

    m, n = len(key), len(lock)
    board = [[0] * (m * 2 + n) for _ in range(m * 2 + n)]

    for i in range(n):
        for j in range(n):
            board[m+i][m+j] = lock[i][j]

    r_key = key
    for _ in range(4):
        r_key = rotate(r_key)

        for i in range(1, m+n):
            for j in range(1, m+n):
                unlock(i, j, r_key)
                if check(): return True
                relock(i, j, r_key)

    return False





print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))  # True