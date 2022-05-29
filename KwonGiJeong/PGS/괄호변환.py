def is_balanced(p):
    balance = 0

    for parenthesis in p:

        if parenthesis == '(':
            balance += 1
        else:
            balance -= 1

    return not(bool(balance))


def is_right(p):
    right = 0

    if is_balanced(p) == False:
        return False

    for parenthesis in p:

        if parenthesis == '(':
            right += 1
        else:
            right -= 1

        if right < 0:
            return False

    return True


def solution(p):

    if is_right(p):
        return p

    for i in range(2, len(p)+1, 2):

        if is_balanced(p[:i]):
            u = p[:i]
            v = p[i:]
            break

    if is_right(u):
        return u + solution(v)

    else:
        result = '(' + solution(v) + ')'
        for i in u[1:-1]:
            if i == '(':
                result += ')'
            else:
                result += '('

    return result
