# PyPy3
import sys

input = lambda: sys.stdin.readline().strip()

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def rotate(st, mod):
    for _ in range(mod):
        tmp = board[st][st]
        cur_r, cur_c = st, st

        k = 0
        while k < 4:
            nxt_r = cur_r + dr[k]
            nxt_c = cur_c + dc[k]
            if nxt_r == st and nxt_c == st:
                break
            if (
                st <= nxt_r
                and nxt_r < N - st
                and st <= nxt_c
                and nxt_c < M - st
            ):
                board[cur_r][cur_c] = board[nxt_r][nxt_c]
                cur_r = nxt_r
                cur_c = nxt_c
            else:
                k += 1
        board[st + 1][st] = tmp


N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

box_cnt = min(N, M) // 2
n, m = N, M
for i in range(box_cnt):
    mod = R % (2 * n + 2 * m - 4)
    rotate(i, mod)
    n -= 2
    m -= 2

for row in board:
    print(" ".join(map(str, row)))
