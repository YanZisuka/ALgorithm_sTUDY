from collections import deque


def solution(rc, operations):

    def shift_row(rc):
        rc = deque(rc)
        tmp = rc.pop()
        rc.appendleft(tmp)
        return list(rc)

    def rotate(rc):
        i, j = 0, 0
        tmp = rc[i][j]
        for _ in range(m-1):
            j += 1
            tmp, rc[i][j] = rc[i][j], tmp
        for _ in range(n-1):
            i += 1
            tmp, rc[i][j] = rc[i][j], tmp
        for _ in range(m-1):
            j -= 1
            tmp, rc[i][j] = rc[i][j], tmp
        for _ in range(n-1):
            i -= 1
            tmp, rc[i][j] = rc[i][j], tmp
        return rc

    n = len(rc)
    m = len(rc[0])

    for operation in operations:
        if operation == 'Rotate':
            rc = rotate(rc)
        elif operation == 'ShiftRow':
            rc = shift_row(rc)

    return rc





print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))
print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]], ["Rotate", "ShiftRow", "ShiftRow"]))
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))