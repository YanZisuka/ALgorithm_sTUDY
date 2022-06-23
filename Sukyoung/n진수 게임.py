def solution(n, t, m, p):
    answer = ''
    change = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    numbers = []
    num = 0

    while len(numbers) <= (m * (t - 1)) + p:
        result = []
        quot = num

        while quot >= n:
            q = quot // n
            r = quot % n
            if r >= 10:
                r = change[r]
            result.append(r)
            quot = q

        if quot >= 10:
            quot = change[quot]
        result.append(quot)

        result.reverse()
        numbers += result
        num += 1

    for i in range(t):
        answer += str(numbers[i * m + p - 1])

    return answer