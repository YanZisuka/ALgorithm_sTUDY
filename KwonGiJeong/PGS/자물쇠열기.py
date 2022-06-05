def solution(key, lock):
    hole = set()
    N = len(lock)
    M = len(key)
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                hole.add((i, j))

    key_hole = []
    for i in range(M):
        for j in range(M):
            if key[i][j] == 1:
                key_hole.append((i, j))

    if len(hole) > len(key_hole):
        return False

    for _ in range(4):
        for y in range(-N + 1, M + N):
            for x in range(-N + 1, M + N):
                answer = set(hole)
                is_valid = True
                for k in key_hole:
                    k_y = k[0] + y
                    k_x = k[1] + x
                    if (k_y, k_x) in answer:
                        answer.remove((k_y, k_x))
                    elif k_y < 0 or k_y >= N or k_x < 0 or k_x >= N:
                        continue
                    else:
                        is_valid = False
                        break

                if len(answer) == 0 and is_valid:
                    return True

        for i in range(len(key_hole)):
            p = key_hole[i]
            key_hole[i] = (M - p[1] - 1, p[0])

    return False
