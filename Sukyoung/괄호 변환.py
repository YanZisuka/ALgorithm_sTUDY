def solution(p):
    answer = []
    p = list(p)

    def is_correct(x):
        cnt = 0
        for i in x:
            if i == '(':
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                return False
        if cnt != 0:
            return False
        else:
            return True

    if is_correct(p):
        return ''.join(p)

    def make_right(x):
        if not x:
            return ''

        open_cnt = 0
        close_cnt = 0

        for i in range(len(x)):
            if x[i] == '(':
                open_cnt += 1
            else:
                close_cnt += 1
            if open_cnt == close_cnt:
                u = x[:i + 1]
                v = x[i + 1:]
                return [u, v]

    uv = make_right(p)
    u = uv[0]
    v = uv[1]

    if is_correct(u):
        v = ''.join(v)
        return ''.join(u + list(solution(v)))

    else:
        answer.append('(')
        answer += solution(v)
        answer.append(')')

        new_u = u[1:-1]

        for k in range(len(new_u)):
            if new_u[k] == '(':
                new_u[k] = ')'
            else:
                new_u[k] = '('
        answer += new_u

        return "".join(answer)