from copy import copy


def solution(key, lock):
    l = len(lock)
    k = len(key)

    if l != k:

        key += [[0] * l for _ in range(l - k)]
        for i in range(k):
            key[i] += [0] * (l - k)

    k = len(key)
    for i in range(l):
        for j in range(l):
            if lock[i][j] == 0:
                lock[i][j] = 1
            else:
                lock[i][j] = 0

    key_90 = [[0] * l for _ in range(l)]
    key_180 = [[0] * l for _ in range(l)]
    key_270 = [[0] * l for _ in range(l)]

    for i in range(k):
        for j in range(k):
            key_90[i][j] = key[k - j - 1][i]
            key_180[i][j] = key[k - i - 1][k - j - 1]
            key_270[i][j] = key[j][k - i - 1]

    def move(mat):

        if mat == lock:
            return True
        for m in range(k):
            new_mat = [[0] * k for _ in range(k)]

            for i in range(1, k):
                new_mat[i] = mat[i - 1]

            if new_mat == lock:
                return True

            mat = new_mat
            copy_mat = copy(new_mat)

            for _ in range(k):
                nnew_mat = [[0] * k for _ in range(k)]
                for r in range(k):
                    for c in range(1, k):
                        nnew_mat[r][c] = copy_mat[r][c - 1]

                if nnew_mat == lock:
                    return True
                copy_mat = nnew_mat

        return False

    if move(key_90):
        return True
    if move(key_180):
        return True
    if move(key_270):
        return True
    return False