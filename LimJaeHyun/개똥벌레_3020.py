import sys

input = sys.stdin.readline

N, H = map(int, input().split())
obstacles = list(int(input()) for _ in range(N))  # 석순, 종유석의 길이를 리스트화

cave = list([0] * N for _ in range(H))  # 동굴 초기화

for height in cave:  # 종유석
    for idx in range(1, len(obstacles) + 1, 2):
        if obstacles[idx] != 0:
            height[idx] = 1
            obstacles[idx] = obstacles[idx] - 1

for i in range(len(cave) - 1, -1, -1):  # 석순
    for j in range(0, len(obstacles), 2):
        if obstacles[j] != 0:
            cave[i][j] = 1
            obstacles[j] = obstacles[j] - 1

how_many_breaks_per_height = []
for row in cave:
    how_many_breaks_per_height.append(sum(row))

print(min(how_many_breaks_per_height), end=' ')
print(how_many_breaks_per_height.count(min(how_many_breaks_per_height)))
