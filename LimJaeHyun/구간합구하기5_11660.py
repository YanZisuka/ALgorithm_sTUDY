import sys

N, M = map(int, input().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for tc in range(1, M + 1):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    sero = abs(x2 - x1) + 1
    garo = abs(y2 - y1) + 1
    guganhap = 0

    for i in range(x1 - 1, x1 + sero - 1):
        for j in range(y1 - 1, y1 + garo - 1):
            guganhap += matrix[i][j]

    print(guganhap)
