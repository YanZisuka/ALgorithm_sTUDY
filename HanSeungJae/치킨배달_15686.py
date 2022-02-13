from itertools import combinations


def chicken_distance(n, m, matrix):
    homes = []
    chicken_houses = []

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                homes.append((i, j))
            elif matrix[i][j] == 2:
                chicken_houses.append((i, j))

    min_val = float('INF')
    for chicken_house in combinations(chicken_houses, m):
        village_total = 0
        for home in homes:
            distances = []
            for position in chicken_house:
                distances.append(abs(home[0]-position[0]) + abs(home[1]-position[1]))
            village_total += min(distances)
            if min_val <= village_total: break
        if min_val > village_total:
            min_val = village_total

    return min_val


n, m = map(int, input().split())
matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

print(chicken_distance(n, m, matrix))
