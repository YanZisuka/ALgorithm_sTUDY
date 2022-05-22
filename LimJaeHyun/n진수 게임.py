import string


def solution(n, t, m, p):
    answer = ''
    total_string = '0'
    tmp = string.digits + string.ascii_lowercase

    def convert(number, base):
        q, r = divmod(number, base)
        if q == 0:
            return tmp[r]
        else:
            return convert(q, base) + tmp[r]

    for i in range(1, t*m):
        total_string += str(convert(i, n)).upper()
    for i in range(p-1, len(total_string), m):
        answer += total_string[i]
        if len(answer) == t:
            break
    return answer


print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))
