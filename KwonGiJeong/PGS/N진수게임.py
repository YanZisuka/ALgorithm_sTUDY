def conversion(num, n):
    numbers = '0123456789ABCDEF'
    if num == 0:
        return '0'

    n_number = ''
    while num > 0:
        n_number = numbers[num % n] + n_number
        num = num // n

    return n_number


def solution(n, t, m, p):
    answer = ''
    temp = ''

    for i in range(t * m):
        temp += conversion(i, n)

    for i in range(t):
        answer += temp[p - 1 + (m * i)]

    return answer
