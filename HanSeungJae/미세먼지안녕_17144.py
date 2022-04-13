import sys
input = sys.stdin.readline

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def diffusion():
    diff = [[0] * c for _ in range(r)]

    for ci in range(r):
        for cj in range(c):
            if room[ci][cj] != -1:
                dust = room[ci][cj] // 5

                for k in range(4):
                    ni = ci + di[k]
                    nj = cj + dj[k]
                    if 0 <= ni < r and 0 <= nj < c and room[ni][nj] != -1:
                        diff[ni][nj] += dust
                        room[ci][cj] -= dust

    for i in range(r):
        for j in range(c):
            room[i][j] += diff[i][j]


def clean(i, j, isUpper):
    j += 1
    tmp = room[i][j]
    room[i][j] = 0

    if isUpper:
        for dir in [3, 0, 2, 1]:
            while True:
                ci, cj = i + di[dir], j + dj[dir]
                if 0 <= ci < r and 0 <= cj < c and room[ci][cj] == -1:
                    return
                if 0 <= ci < r and 0 <= cj < c:
                    room[ci][cj], tmp = tmp, room[ci][cj]
                else:
                    break
                i, j = ci, cj
    else:
        for dir in [3, 1, 2, 0]:
            while True:
                ci, cj = i + di[dir], j + dj[dir]
                if 0 <= ci < r and 0 <= cj < c and room[ci][cj] == -1:
                    return
                if 0 <= ci < r and 0 <= cj < c:
                    room[ci][cj], tmp = tmp, room[ci][cj]
                else:
                    break
                i, j = ci, cj


r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]
isUpper = True
cleaners = []
answer = 2

for i in range(r):
    for j in range(c):
        if room[i][j] == -1:
            cleaners.append((i, j, isUpper))
            isUpper = False

while t:
    diffusion()
    for cleaner in cleaners:
        clean(*cleaner)
    t -= 1

for i in range(r):
    answer += sum(room[i])

print(answer)