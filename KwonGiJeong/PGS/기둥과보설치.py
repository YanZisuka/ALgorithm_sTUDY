def solution(n, build_frame):
    answer = []
    pillar = [[0]*(n+1) for _ in range(n)]
    beam = [[0]*(n) for _ in range(n+1)]

    def check(i, j, a):
        if a:
            if pillar[i][j] or pillar[i][j+1] or ((j-1 != -1 and beam[i][j-1]) and (j+1 != n and beam[i][j+1])):
                return True
        else:
            if i+1 == n or pillar[i+1][j] or (j-1 != -1 and beam[i+1][j-1]) or (j != n and beam[i+1][j]):
                return True
        return False

    for j, i, a, b in build_frame:
        i = n-i
        if b:
            if a:
                if check(i, j, a):
                    beam[i][j] = 1
            else:
                if check(i-1, j, a):
                    pillar[i-1][j] = 1
        else:
            if a:
                beam[i][j] = 0
                if not((j-1 == -1 or not beam[i][j-1] or check(i, j-1, 1)) and (j+1 == n or not beam[i][j+1] or check(i, j+1, 1)) and (not pillar[i-1][j] or check(i-1, j, 0)) and (not pillar[i-1][j+1] or check(i-1, j+1, 0))):
                    beam[i][j] = 1
            else:
                pillar[i-1][j] = 0
                if not((j-1 == -1 or not beam[i-1][j-1] or check(i-1, j-1, 1)) and (j == n or not beam[i-1][j] or check(i-1, j, 1)) and (i-2 == -1 or not pillar[i-2][j] or check(i-2, j, 0))):
                    pillar[i-1][j] = 1
    for i in range(n):
        for j in range(n+1):
            if pillar[i][j]:
                answer.append([j, n-i-1, 0])
    for i in range(n+1):
        for j in range(n):
            if beam[i][j]:
                answer.append([j, n-i, 1])
    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return answer
