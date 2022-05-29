def solution(n, s, a, b, fares):
    answer = 0
    road = [[float('inf')] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                road[i][j] = 0

    for fare in fares:
        road[fare[0]][fare[1]] = fare[2]
        road[fare[1]][fare[0]] = fare[2]

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                road[i][j] = min(road[i][j], road[i][k] + road[k][j])

    case = []
    for i in range(1, n + 1):
        case.append(road[s][i] + road[i][a] + road[i][b])
    answer = min(case)

    return answer